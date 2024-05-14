''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 1 challenge (challenge2.py).  
''' 

numberToBeRoundUp = input("Enter a number:")
floatNumberToBeRoundUp = float(numberToBeRoundUp)
intNumberToBeRoundUp = int(floatNumberToBeRoundUp)
decimalPoints = floatNumberToBeRoundUp-intNumberToBeRoundUp

if decimalPoints < 0.5:
    print("Rounded value is: "+str(intNumberToBeRoundUp))
else:
    print("Rounded value is: "+str(intNumberToBeRoundUp+1))