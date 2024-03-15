import random
import html
from typing import List


class Question:
    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer


class TriviaQuestion:
    def __init__(
        self,
        type: str,
        difficulty: str,
        category: str,
        question: str,
        correct_answer: str,
        incorrect_answers: List[str],
    ) -> None:
        self.question_type = type
        self.difficulty = difficulty
        self.category = category
        self.question = question
        self.incorrect_answers = incorrect_answers
        self.response = None

        if category == "boolean":
            self.correct_answer = True if correct_answer == "True" else False
        else:
            self.correct_answer = correct_answer

    def ask(self) -> bool:
        print(f"{html.unescape(self.question)}")
        if self.question_type == "boolean":
            self.response = input("true or false?\n> ")
        else:
            print("Options:")
            answers = self.scramble_responses()
            for index, value in enumerate(answers):
                print(f"{index}. {value}")
            self.response = input("\nResponse:\n> ")
            try:
                int_response = int(self.response)
                self.response = answers[int_response]
            except:
                pass
        return self.response.lower() == self.correct_answer.lower()

    def scramble_responses(self) -> List[str]:
        temp_list = self.incorrect_answers.copy()
        temp_list.append(self.correct_answer)
        random.shuffle(temp_list)
        return temp_list
