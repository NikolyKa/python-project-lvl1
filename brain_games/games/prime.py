from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
END = 100


def start():
    first_num = randint(START, END)
    d = 2
    c_ans = 'no'
    while first_num % d != 0:
        d += 1
        if d == first_num:
            c_ans = 'yes'
    question_text = f'{first_num}'
    return c_ans, question_text
