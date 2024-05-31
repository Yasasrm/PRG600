''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 1 Question 6 (challenge3.py).
''' 

binNumber = "0b"

def binaryConverter(dcml): #convert decimal to binary
    quotient = int(dcml)/2
    remainder = int(dcml)%2
    if quotient > 0:
        binaryDigir = remainder
        binaryConverter(quotient)
        global binNumber
        binNumber += str(binaryDigir)

#entry point
if __name__ == "__main__":
    decimalNumber = input("Enter a decimal number: ") #get decimal number
    binaryConverter(decimalNumber) #convert decimal number to binary with the custom fuction
    print(binNumber) #print custom function binary value
    print(bin(int(decimalNumber))) #print buildin function binary value