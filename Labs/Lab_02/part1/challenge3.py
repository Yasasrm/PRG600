''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 6 (challenge3.py).
''' 

binNumber = "0b"

def main():
    decimalNumber = input("Enter a decimal number: ")
    binaryConverter(decimalNumber)
    print(binNumber)
    print(bin(int(decimalNumber)))


def binaryConverter(dcml):
    quotient = int(dcml)/2
    remainder = int(dcml)%2
    if quotient > 0:
        binaryDigir = remainder
        binaryConverter(quotient)
        global binNumber
        binNumber += str(binaryDigir)

#entry point
if __name__ == "__main__":
    main()