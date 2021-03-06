from prompt import string

ROUND_COUNT = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for i in range(ROUND_COUNT):
        correct_answer, question_text = game.start()
        print(f'Question: {question_text}')
        answer = string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
