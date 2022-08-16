# Dice Game

import random

import time

#Functions
def roll_dice(n):
    dice = [] 
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

def winner(cdice_list, udice_list):
    computer_total =sum (cdice_list)
    user_total = sum(udice_list)
    if user_total%2!=0 and computer_total%2!=0:
        print('You both lose. :p')
    elif user_total < number_dice*3 and computer_total <number_dice*3:
        print('You both lose. :p')
    elif user_total%2==0 and user_total > number_dice*3 :
        print('User wins with a score of',user_total,'!')
        print("   W   ")
        print("\(^.^)/")
    elif computer_total%2==0  and computer_total > number_dice*3:
        print('Computer wins with a score of', computer_total,'!')
        print("(~0.0)~(/x.x)/")
    else:
     print("It's a tie try again")

def roll_again(choices, dice_list):
     print('Good luck!')
     time.sleep(1)
     for i in range(len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1,6)
        time.sleep(1)

def computer_strategy(n):
    print('What will the computer decide? ...')
    time.sleep(2)
    choices = '' 
    for i in range(n):
        if computer_rolls[i]%2==0:
            choices = choices + '-'
        else:
            choices = choices + 'r'
    return choices

#start game
number_dice = input('Enter number of dice:')
number_dice = int(number_dice)
print('Game Rules! \nTo win the total score has to be both even and greater than:'
      ,number_dice*3,)
ready = input('Press any key to play')



#User turn 
user_rolls = roll_dice(number_dice)
print('User first roll: ', user_rolls)


user_choices = input("Enter - to hold or r to roll again :")

while len(user_choices) != number_dice:
    print('You must enter', number_dice, \
    'choices')
    user_choices = input("Enter - to hold or r \
    to roll again :")

roll_again(user_choices, user_rolls)
print('Players final roll: ', user_rolls)

# Computer's turn 
print('Computers turn ')
computer_rolls = roll_dice(number_dice)
print('Computer first roll: ', computer_rolls)

computer_choices = computer_strategy(number_dice)
print('Computer Choice: ', computer_choices)

roll_again(computer_choices, computer_rolls)
print('Computer final roll: ', computer_rolls)

#Winner
winner(computer_rolls,user_rolls)
