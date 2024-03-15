from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from trivia_brain import TriviaBrain
import aiohttp
import asyncio

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))


brain = TriviaBrain()


async def main_loop():
    while True:
        await brain.new_game()
        brain.main_loop()
        print(f"You answered {brain.correct_answers} out of {brain.total_questions}\n")
        play_again = input("play again? y/n\n> ")
        if play_again != "y":
            break


asyncio.run(main_loop())
