from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 100


def start():
    num = randint(START, END)
    question_text = num
    if num % 2 == 0:
        c_ans = 'yes'
    else:
        c_ans = 'no'
    return c_ans, question_text
