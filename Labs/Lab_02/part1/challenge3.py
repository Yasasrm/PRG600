''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 6 (challenge3.py).
''' 

def main():
    decimalNumber = input("Enter a decimal number: ")
    binaryConverter(decimalNumber)


def binaryConverter(dcml):
    quotient = int(dcml)/2
    remainder = int(dcml)%2
    if quotient != 1:
        binaryDigir = remainder
        binaryConverter(binaryDigir)
    else:
        binaryDigir = quotient
    return 0
