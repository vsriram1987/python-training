'''
Created on 17-Dec-2018

@author: vsrir
'''
#Make the user guess a random number between 1 to 100

from random import randint
randnumber = randint(1,100)
guess = int(input("Enter your guessed number:"))
attempts = 1
teasecount = 1
while guess != randnumber:
    if guess < 0:
        attempts -= 1
        confirmation = input("Are you sure you want to give up?").upper()
        if confirmation == "Y":
            print(f"Hmm...giving up so early! Just {attempts} attempts. \n --GAME OVER--")
            break
    elif guess > 100:
        print("Stay between 1 and 100 please!")
    elif 0<abs(guess-randnumber)<10:
        teasecount = 1
        print("Getting closer!")
    elif abs(guess-randnumber)>10:
        teasecount += 1
        print("Nah! Too far!")
    attempts += 1
    if teasecount > 3:
        print("You don't seem to be very good at it! Enter a negative number to give up...")
        teasecount = 1
    guess = int(input("Enter your guessed number:"))
if guess == randnumber:
    print(f"Bingo!!! You found it in {attempts} attempts.")