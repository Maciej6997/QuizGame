from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [Question(quest['text'],quest['answer'])  for  quest in  question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print('You complted quiz')
print(f'Your final score was {quiz.score}/{quiz.question_number}')
