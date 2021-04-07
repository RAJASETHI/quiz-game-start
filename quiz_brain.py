class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score_count = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(guess, current_question.answer)
            # self.score_count += 1

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it Right!")
            self.score_count += 1
            # return True
        else:
            print("That's Wrong.")
            # return False
        print(f"The Correct answer was {correct_answer}")
        print(f"The Current Score is:{self.score_count}/{self.question_number}")

