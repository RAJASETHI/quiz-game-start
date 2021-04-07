from data import question_data
from question_model import question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(question(i["question"], i["correct_answer"]))
# print(question_bank[1].text,question_bank[1].answer)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("\n\nYou have Completed the quiz")
print(f"Your Final Score was:{quiz.score_count}/{quiz.question_number}")

