from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

brain = QuizBrain(question_bank)

while True:
    question = brain.NextQuestion()

    if not question:
        break

    answer = (
        True
        if input(f"\nQ.{brain.question_number}: {question.text}? y/n\n> ") == "y"
        else False
    )
    brain.IsRightAnswer(question, answer)
    print(f"{brain.correct_answers} correct of {brain.question_number} asked\n")
