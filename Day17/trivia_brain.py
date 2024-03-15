import aiohttp
import random
from prettytable import PrettyTable
from typing import List
from question_model import TriviaQuestion

categories = [
    {"id": None, "label": "Any"},
    {"id": 9, "label": "General Knowledge"},
    {"id": 10, "label": "Entertainment: Books"},
    {"id": 11, "label": "Entertainment: Film"},
    {"id": 12, "label": "Entertainment: Music"},
    {"id": 13, "label": "Entertainment: Musicals & Theatres"},
    {"id": 14, "label": "Entertainment: Television"},
    {"id": 15, "label": "Entertainment: Video Games"},
    {"id": 16, "label": "Entertainment: Board Games"},
    {"id": 29, "label": "Entertainment: Comics"},
    {"id": 31, "label": "Entertainment: Japanese Anime & Manga"},
    {"id": 32, "label": "Entertainment: Cartoon & Animations"},
    {"id": 17, "label": "Science and Nature"},
    {"id": 18, "label": "Science: Comuputers"},
    {"id": 19, "label": "Science: Mathematics"},
    {"id": 30, "label": "Science: Gadgets"},
    {"id": 20, "label": "Mythology"},
    {"id": 21, "label": "Sports"},
    {"id": 22, "label": "Geography"},
    {"id": 23, "label": "History"},
    {"id": 24, "label": "Politics"},
    {"id": 25, "label": "Art"},
    {"id": 26, "label": "Celebrities"},
    {"id": 27, "label": "Animals"},
    {"id": 28, "label": "Vehicles"},
]

difficulty = ["easy", "medium", "hard", "all"]

trivia_type = [
    {"label": "Any", "id": None},
    {"label": "True/False", "id": "boolean"},
    {"label": "Multiple Choice", "id": "multiple"},
]

api_codes = [
    {"id":0, "msg": "Success."},
    {"id":1, "msg": "No Results Could not return results. The API doesn't have enough questions for your query."},
    {"id":2, "msg": "Invalid Parameter Contains an invalid parameter. Arguements passed in aren't valid."},
    {"id":3, "msg": "Token Not Found Session Token does not exist."},
    {"id":4, "msg": "Token Empty Session Token has returned all possible questions for the specified query."},
    {"id":5, "msg": "Rate Limit Too many requests have occurred. Each IP can only access the API once every 5 seconds."},
]

difficulty_table = PrettyTable()
difficulty_table.field_names=["difficulty"]
for dif in difficulty:
    difficulty_table.add_row([dif])

class TriviaBrain:

    def __init__(self) -> None:
        self.total_questions = 0
        self.category = None
        self.correct_answers = 0
        self.categories = self.create_category_table()
        self.trivia_types = self.create_trivia_type_categories()
        self.selected_trivia_type = None
        self.difficulty = None
        self.question_bank: List[TriviaQuestion] = []

    def create_category_table(self):
        table = PrettyTable()
        table.field_names = ["id", "category"]
        for index, category in enumerate(categories):
            table.add_row([index, category["label"]])
        return table

    def create_trivia_type_categories(self):
        table = PrettyTable()
        table.field_names = ["id", "type"]
        for index, value in enumerate(trivia_type):
            table.add_row([index, value["label"]])
        return table

    async def new_game(self):
        self.correct_answers = 0
        self.total_questions = self.prompt_for_how_many_questions()
        self.category = self.prompt_for_category()
        self.selected_trivia_type = self.prompt_for_trivia_type()
        self.difficulty = self.prompt_for_difficulty()
        data = await self.fetch_questions()
        if data["response_code"] != 0:
            print(self.get_api_message(data["response_code"]))
            return

        self.process_data(data)

    def main_loop(self):
        while True:
            remaining_questions = len(self.question_bank)
            if remaining_questions == 0:
                break

            question: TriviaQuestion = self.question_bank.pop(random.randint(0, remaining_questions - 1))
            if question.ask():
                self.correct_answers += 1
                print("Correct!\n")
            else:
                print("Incorrect :(\n")

    def prompt_for_how_many_questions(self):
        while True:
            total = input("how many questions for the trivia?\n> ")
            if total == 0 or not total.isdigit():
                print("Invalid input, try again\n")
            else:
                return total

    def prompt_for_category(self):
        while True:
            index = input(
                f"Select an id for the category from the list below:\n{self.categories}\n> "
            )
            if not index.isdigit() or int(index) >= len(categories) :
                print("That's not a valid id, please try again\n")
            else:
                return categories[int(index)]

    def prompt_for_trivia_type(self):
        while True:
            index = input(f"Select trivia type:\n{self.trivia_types}\n> ")
            if  not  index.isdigit() or int(index) >= len(trivia_type) :
                print("That's not a valid choice, try again\n")
            else:
                return trivia_type[int(index)]
        
    def prompt_for_difficulty(self):
        while True:
            print(f"Select difficulty:\n{difficulty_table}\n")
            selection = input(f"> ")
            if selection not in difficulty:
                print("Invalid option\n")
            else:
                return selection

    async def fetch_questions(self):
        url = f"https://opentdb.com/api.php?amount={self.total_questions}"
        if self.category["id"] != None:
            url += f"&category={self.category["id"]}"
        if self.difficulty != "all":
            url += f"&difficulty={self.difficulty}"
        if self.selected_trivia_type["id"] != None:
            url += f"&type={self.selected_trivia_type["id"]}"

        #print(f"url: {url}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
            
    def process_data(self, data) -> List[TriviaQuestion]:
        results = data["results"]
        self.question_bank.clear()
        for result in results:
            type = result["type"]
            difficulty = result["difficulty"]
            category = result["category"]
            question = result["question"]
            correct_answer = result["correct_answer"]
            incorrect_answers = result["incorrect_answers"]

            self.question_bank.append(TriviaQuestion(type,difficulty, category, question, correct_answer, incorrect_answers))


    def get_api_message(self, code) -> str:
        for value in api_codes:
            if value["id"] == code:
                return value["message"]
        return "Something went wrong, please try again"
