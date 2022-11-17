# Quizzler

import data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = [
    Question(dic["question"], dic["correct_answer"])
    for dic in data.load_data()
]

# initialize the quiz brain
qb = QuizBrain(question_bank)
# initialize the GUI
qi = QuizInterface(qb)
