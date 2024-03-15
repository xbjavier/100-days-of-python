import random

from question_model import Question
from typing import List


class QuizBrain:
    def __init__(self, question_list: List[Question]) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.correct_answers = 0

    def NextQuestion(self) -> Question:
        questions_list_len = len(self.question_list)
        if questions_list_len == 0:
            return None

        random_question = random.randint(0, questions_list_len - 1)
        question = self.question_list.pop(random_question)
        self.question_number += 1
        return question

    def IsRightAnswer(self, question: Question, answer: bool) -> bool:
        expected = True if question.answer == "True" else False
        if answer == expected:
            self.correct_answers += 1
            return True
        return False
