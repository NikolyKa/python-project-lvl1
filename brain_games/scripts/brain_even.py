#!/usr/bin/env python
import prompt
from random import randint


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    a = randint(0, 9)
    print('Question:', a)
    if a % 2 == 0:
        qe = input('Your answer: ')
        if qe.lower() == 'yes':
            print('Correct!')
        else:
            return(f'''"no" is wrong answer ;(. Correct answer was "yes".')
Let`s try again, {name}''')
    else:
        qe = input('Your answer: ')
        if qe.lower() == 'no':
            print('Correct!')
        else:
            return (f'''"yes" is wrong answer ;(. Correct answer was "no".')
Let`s try again, {name}''')
    a2 = randint(0, 9)
    print('Question:', a2)
    if a2 % 2 == 0:
        qe = input('Your answer: ')
        if qe.lower() == 'yes':
            print('Correct!')
        else:
            return (f'''"no" is wrong answer ;(. Correct answer was "yes".')
Let`s try again, {name}''')
    else:
        qe = input('Your answer: ')
        if qe.lower() == 'no':
            print('Correct!')
        else:
            return (f'''"yes" is wrong answer ;(. Correct answer was "no".')
Let`s try again, {name}''')
    a3 = randint(0, 9)
    print('Question:', a3)
    if a3 % 2 == 0:
        qe = input('Your answer: ')
        if qe.lower() == 'yes':
            print('Correct!')
            return f'Congratulations, {name}!'
        else:
            return (f'''"no" is wrong answer ;(. Correct answer was "yes".')
Let`s try again, {name}''')
    else:
        qe = input('Your answer: ')
        if qe.lower() == 'no':
            print('Correct!')
            return f'Congratulations, {name}!'
        else:
            return (f'''"yes" is wrong answer ;(. Correct answer was "no".')
Let`s try again, {name}''')


def main():
    print(brain_even())
	
	
if __name__=='__main__':
    main()
