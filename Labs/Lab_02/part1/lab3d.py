''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 4 (lab3d.py).  
''' 

from random import randint

#variable initialization
secret = randint(1,10)

while True:
    user_guess = input("Guess a number between 1 and 10:") #user input
    if secret == int(user_guess):
        print("Correct! You win.")
        break #exit point
    else:
        print("Sorry, that's not it.") #loop continues