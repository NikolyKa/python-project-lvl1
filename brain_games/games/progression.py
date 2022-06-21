from random import randint

DESCRIPTION = 'What number is missing in this progression?'


def start():
    first_num = randint(1, 20)
    second_num = randint(2, 10)
    lists = ''
    index = randint(0, 9)
    for n in range(10):
        first_num += second_num
        lists += str(first_num) + ' '
    new = lists.split(" ")
    correct_answer = new[index]
    new[index] = '..'
    mean = (' '.join(new))
    question_text = f'{mean}'
    return correct_answer, question_text
