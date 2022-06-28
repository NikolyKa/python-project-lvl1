from random import randint

DESCRIPTION = 'What number is missing in this progression?'
START_FIRST_NUM = 1
END_FIRST_NUM = 20
START_STEP_NUM = 2
END_STEP_NUM = 10


def start():
    first_num = randint(START_FIRST_NUM, END_FIRST_NUM)
    step_num = randint(START_STEP_NUM, END_STEP_NUM)
    line = ''
    index = randint(0, 9)
    for i in range(10):
        first_num += step_num
        line += str(first_num) + ' '
    new = line.split(" ")
    correct_answer = new[index]
    new[index] = '..'
    connection = (' '.join(new))
    question_text = f'{connection}'
    return correct_answer, question_text
