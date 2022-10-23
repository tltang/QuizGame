class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(player_answer, current_question.answer)

    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            return False
        else:
            return True

    def check_answer(self, player_answer, correct_answer):
        if player_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong, correct answer is: {correct_answer}")

        print(f"Current Score: {self.score}/{self.question_number}")
        print("\n")
