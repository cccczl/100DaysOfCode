# Quiz

import data
from question_model import Question
from quiz_brain import QuizBrain


# switch to True to use the original questions
use_original = False

question_bank = []
# fill up the question bank list with Question objects
if use_original:
    question_bank.extend(
        Question(dic["text"], dic["answer"])
        for dic in data.original_question_data
    )

else:
    question_bank.extend(
        Question(dic["question"], dic["correct_answer"])
        for dic in data.question_data
    )

qb = QuizBrain(question_bank)
# repeat while there are still questions remaining
while qb.still_has_questions():
    qb.next_question()
# no need for a + 1 to the question_number here, as it gets increased after the last question is completed
print(f"Your final score is: {qb.score}/{qb.question_number}.")
