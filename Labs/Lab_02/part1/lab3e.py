''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 5 (lab3e.py).
Math Quiz v2.0  
''' 

import random
from random import randint

sum = 0 
print("SUMMING CALCULATOR") 
while True: 
    print("The sum so far: " + str(sum)) 
    user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") #get user input
    if user_input == "": #exit point
        break 
    else:  #summing calculation
        sum += int(user_input) 
print("Thank you for using summing calculator. The final sum was " + str(sum) #output
+ ".")


