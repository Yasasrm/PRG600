''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 1 (lab3a.py).  
''' 

points = 0
#Question 1
num = 0  
while num != 26: 
    user_input = input("Enter the answer to 12 + 14, or press 's' to skip: ") #User input
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

#Question 2
num = 0  
while num != 31: 
    user_input = input("Enter the answer to 23 + 8, or press 's' to skip: ") #User input
    if user_input == 's': #Skip the question
        break 
    else: 
        num = int(user_input) 
    if num != 31: #Incorrect answer
        print("Incorrect. Try again.") 
    else: #correct answer
        print("Correct! You have been awarded 1 point!") 
        points+=1
print("Next question...")

#Question 3
num = 0  
while num != 43: 
    user_input = input("Enter the answer to 30 + 13, or press 's' to skip: ") #User input
    if user_input == 's': #Skip the question
        break 
    else: 
        num = int(user_input) 
    if num != 43: #Incorrect answer
        print("Incorrect. Try again.") 
    else: #correct answer
        print("Correct! You have been awarded 1 point!") 
        points+=1
print("Next question...")

#Question 4
num = 0  
while num != 44: 
    user_input = input("Enter the answer to 17 + 27, or press 's' to skip: ") #User input
    if user_input == 's': #Skip the question
        break 
    else: 
        num = int(user_input) 
    if num != 44: #Incorrect answer
        print("Incorrect. Try again.") 
    else: #correct answer
        print("Correct! You have been awarded 1 point!") 
        points+=1
print("Next question...")

print("You received a grade of "+str((points/4)*100)+"%.") #Final output