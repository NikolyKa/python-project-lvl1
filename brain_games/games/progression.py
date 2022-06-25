from random import randint

DESCRIPTION = 'What number is missing in this progression?'
START_FIRST_NUM = 1
END_FIRST_NUM = 20
START_SECOND_NUM = 2
END_SECOND_NUM = 10


def start():
    first_num = randint(START_FIRST_NUM, END_FIRST_NUM)
    second_num = randint(START_SECOND_NUM, END_SECOND_NUM)
    lists = ''
    index = randint(0, 9)
    for n in range(10):
        first_num += second_num
        lists += str(first_num) + ' '
    new = lists.split(" ")
    c_ans = new[index]
    new[index] = '..'
    mean = (' '.join(new))
    question_text = f'{mean}'
    return c_ans, question_text
