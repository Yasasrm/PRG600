''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 3 Question 1 (lab5a.py).  
''' 

user_numbers = [] 
print("SUMMING CALCULATOR") 
while True: 
    user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") 
    if user_input == "": 
        break 
    else:  
        user_numbers.append(int(user_input)) 
print(user_numbers) 
print("Thank you for using summing calculator. The final sum was " + str(sum(user_numbers)) + ".") 