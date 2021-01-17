#!/usr/bin/env python
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# question_bank = [Question(**q) for q in question_data]   # not taught yet...
question_bank = []
for question in question_data:
    # question_bank.append(Question(**question))   # ** not taught yet..
    # question_bank.append(Question(question["text"], question["answer"]))
    question_bank.append(
        Question(question["question"], question["correct_answer"])
    )

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
