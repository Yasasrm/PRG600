''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 5 (lab3e.py).
Math Quiz v2.0  
''' 

import random
from random import randint

points = 0
#Question 1
num = 0  
while num != 26: 
    user_input = input("Enter the answer to 1 + 6, press 's' to skip or 'q' to quit: ") #User input
    if user_input == 's': #Skip the question
        break 
    else: 
        num = int(user_input) 
    if num != 26: #Incorrect answer
        print("Incorrect. Try again.") 
    else: #correct answer
        print("Correct! You have been awarded 1 point!") 
        points+=1
print("Next question...")

print("Quiz over. You scored 50.0%.")


