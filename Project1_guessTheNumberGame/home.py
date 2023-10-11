# Name : Raisun Lakra
# Objective : guess the no in three chances

import random

print("####################### Game: Guess the Number #######################")

play = 'y'
while play in ['Y', 'y']:
    print('Game: Given two numbers, an upper limit and a lower limit, you have to guess the number between them.')
    print('You have 3 chances to win.')
    print('')

    lowerLimit = random.randint(1, 1000)
    upperLimit = lowerLimit + random.randint(5, 10)

    print(f'Upper Limit: {upperLimit}')
    print(f'Lower Limit: {lowerLimit}')

    ans = random.randint(lowerLimit, upperLimit)
    chances = 3

    while chances > 0:
        guess = int(input(f'Enter your guess ({chances} chances left): '))
        if guess == ans:
            print('Correct!')
            print('You win!')
            break
        elif guess < ans - 3:
            print('Your guess is way too low.')
        elif guess < ans:
            print('Your guess is low.')
        elif guess > ans + 3:
            print('Your guess is way too high.')
        else:
            print('Your guess is high.')
        chances -= 1

    if chances == 0:
        print(f'You ran out of chances. The correct answer was {ans}. Better luck next time!')

    play = input('Enter [Y/y] to play again: ')

    # -------- E N D -----------