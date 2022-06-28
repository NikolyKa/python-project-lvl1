from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 100


def start():
    num = randint(START, END)
    question_text = num
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question_text
