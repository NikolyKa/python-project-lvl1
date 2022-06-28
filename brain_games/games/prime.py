from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
END = 100


def start():
    first_num = randint(START, END)
    counter = 2
    correct_answer = 'no'
    while first_num % counter != 0:
        counter += 1
        if counter == first_num:
            correct_answer = 'yes'
    question_text = f'{first_num}'
    return correct_answer, question_text
