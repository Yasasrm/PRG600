''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 2 Question 3 (lab4c.py).  
''' 

import math

def circle_area(radius): #calculate circle area
    return math.pi * radius**2

if __name__ == "__main__":
    print("Circle Area Calculator")
    cycle = 0
    while True:
        radius = input("Enter a radius between 0 and 1999. Press Enter to exit:")
        if radius.isnumeric() and 0 <= int(radius) < 1000: #validate radius range
            area = circle_area(int(radius))
            print("Radius: %s. Area: %s." %(radius,area))
        elif radius == "" and cycle > 0: #exit point
            print("Exiting...")
            break
        elif radius == "" and cycle == 0: #exit point (first time)
           print("Program was cancelled.")
           break 
        elif radius.isnumeric():
            print("Error: %s is out of bounds." %radius) #if radius not in the range, returns an error
        else:
            print("Error: %s is not a number." %radius) #if radius not a numeric value, returns an error
        cycle+=1


