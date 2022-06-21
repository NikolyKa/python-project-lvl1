#!/usr/bin/env python
from random import randint
from random import choice

DESCRIPTION = 'What is the result of the expression?'


def start():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    symbol = choice('*-+')
    question_text = str(eval(f'{first_num}{symbol}{second_num}'))
    correct_answer = f'{first_num} {symbol} {second_num}'
    return question_text, correct_answer
