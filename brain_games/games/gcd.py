from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
START = 1
END = 100


def start():
    first_num = randint(START, END)
    second_num = randint(START, END)
    question_text = f'{first_num} {second_num}'
    if first_num > second_num:
        temp = second_num
    else:
        temp = first_num
    for i in range(1, temp + 1):
        if (first_num % i == 0) and (second_num % i == 0):
            correct_answer = str(i)
    return correct_answer, question_text
