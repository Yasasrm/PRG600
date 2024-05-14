''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 1 challenge (challenge2.py).  
''' 

numberToBeRoundUp = input("Enter a number:")                #Get a number as user input
floatNumberToBeRoundUp = float(numberToBeRoundUp)           #Convert user input to a float
intNumberToBeRoundUp = int(floatNumberToBeRoundUp)          #Get the integer part of the user input value
decimalPoints = floatNumberToBeRoundUp-intNumberToBeRoundUp #Get the decimal points of the user input value 

#Check the decimal point > 0.5 and add 1 or remove decimal parts from the output and print the output
if decimalPoints < 0.5:
    print("Rounded value is: "+str(intNumberToBeRoundUp))
else:
    print("Rounded value is: "+str(intNumberToBeRoundUp+1))