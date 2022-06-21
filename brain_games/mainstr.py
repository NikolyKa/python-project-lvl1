from prompt import string


def base(game):
    print("Welcome to the Brain Games!")
    name = string('May i have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for i in range(3):
        correct_answer, question_text = game.start()
        print(f'Question: {question_text}')
        answer = string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let`s try again, {name}!""")
            return
    print(f'Congratulations, {name}!')
