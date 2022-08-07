from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []

for q in question_data:
    questions.append(Question(q["text"],q["answer"]))

quizz = QuizBrain(questions)

while quizz.still_has_questions():
    quizz.next_question()

print("You've comepleted the quizz")
print(f"Total score is {quizz.score}/{len(quizz.question_list)}\n")