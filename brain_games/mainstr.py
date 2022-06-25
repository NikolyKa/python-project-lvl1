from prompt import string

ROUNDS = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for i in range(ROUNDS):
        c_ans, question_text = game.start()
        print(f'Question: {question_text}')
        ans = string('Your answer: ')
        if ans == c_ans:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{c_ans}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
