#!/usr/bin/env python
from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def start():
    num = randint(1, 100)
    question_text = num
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question_text
