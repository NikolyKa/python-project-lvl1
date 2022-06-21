from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start():
    first_num = randint(1, 100)
    d = 2
    correct_answer = 'no'
    while first_num % d != 0:
        d += 1
        if d == first_num:
            correct_answer = 'yes'
    question_text = f'{first_num}'
    return correct_answer, question_text
