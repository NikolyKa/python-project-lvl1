from random import randint
from random import choice

DESCRIPTION = 'What is the result of the expression?'
START = 1
END = 100


def start():
    first_num = randint(START, END)
    second_num = randint(START, END)
    symbol = choice('*-+')
    if symbol == '+':
        c_ans = str(first_num + second_num)
    elif symbol == '*':
        c_ans = str(first_num * second_num)
    elif symbol == '-':
        c_ans = str(first_num - second_num)
    question_text = f'{first_num} {symbol} {second_num}'
    return c_ans, question_text
