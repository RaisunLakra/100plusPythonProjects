# Name : Raisun Lakra
# Objective : Build game Rock, Paper, Scissor

import random

print("\t\t\t Rock Paper Scissor \t\t")

play = 'y'
score = 0

choices = ['Rock', 'Paper', 'Scissor']

while play not in ['n','N']:
    print("Enter 1 : Rock, 2 : Paper 3 : Scissor.")
    user = int(input())
    computer = random.randint(1,3)
    if(user > 3 or user < 1):
        print("Invalid input")
    else :
        print(f'Your choice {choices[user-1]}')
        print(f'Computer choice {choices[computer-1]}')
        if computer == user + 1 : 
            print("Computer wins.")
        elif computer == user : 
            print("It is a Tie")
        else :
            print("You win")
            score += 1
    play = input("Enter ['n'/'N'] to quit. ")
print(f"You score is {score}")