''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 3 Question 5 (lab5e.py).  
''' 

import sys 

if len(sys.argv) == 1: 
    print("No arguments found.") 
    sys.exit(0)
else: 
    sum = 0
    count = 0
    for arg in sys.argv[1:]:  # start from the second item in the list 
        if arg.isnumeric():
            print(f"Number found: {arg}.")
            sum += int(arg)
            count += 1
        else:
            print(f"Error: {arg} is not a number.")
print(f"Average for {count} numbers: {sum/count}")