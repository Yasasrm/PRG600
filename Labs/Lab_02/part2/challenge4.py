''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 2 Question 4 (challenge.py).  
''' 

def rtrn_slope(x1, y1, x2, y2): #calculate slope
    if (x2 - x1) != 0:
        return (y2 - y1)/(x2 - x1)
    else:
        return "tan(90)"

def isValidCoordinate(input): #validate coordinates
    if input.isnumeric() and 0 <= int(input) < 11: #check numeric range
        return True
    elif not input.isnumeric(): #if not numeric returns error
        print("Error: %s is not a number." %input)
        return False
    else:
        print("Error: %s is out of bounds." %input) #if out of range returns error
        return False

if __name__ == "__main__":
    while True:
        x1 = input("Enter the starting X value:") #get X1
        if isValidCoordinate(x1):
            break

    while True:
        y1 = input("Enter the next Y value:") #get Y1
        if isValidCoordinate(y1):
            break
    
    while True:
        while True:
            x2 = input("Enter the starting X value:") #get X2
            if isValidCoordinate(x2):
                break
        
        while True:
            y2 = input("Enter the next Y value:") #getY2
            if isValidCoordinate(y2):
                break

        print("Slope is: "+str(rtrn_slope(int(x1), int(y1), int(x2), int(y2)))) #final output