class QuizBrain:

    def __init__(self, question_list) -> None:

        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self) -> bool:

        return self.question_number < len(self.question_list)

    def check_answer(self, answer_to_check, answer) -> None:

        if answer_to_check.lower() == answer.lower():
            print("U got it")
            self.score += 1

        else:
            print("U didn't get it")
        print(f"The correct answer was {answer}")
        print(f"Your score is {self.score}/{self.question_number + 1}\n")

    def next_question(self) -> None:

       current_question = self.question_list[self.question_number]
       answer = input(f"Q.{self.question_number + 1} {current_question.question} (True or Flase): ")
       self.check_answer(answer,current_question.answer)
       self.question_number += 1