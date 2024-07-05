''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 4 Question 4 (challenge6.py).  
''' 

import sys

def letterFilter(fileName):
    try:
        f = open(fileName, 'r')  #Create a file object (read)
        content = f.readlines()  #Load file content
        f.close() #Close file object
        for _, line in enumerate(content):
            print(sorted("".join(word.lower() for word in line.split() if not isNumber(word)))[-1]) #Print alphabetical character that comes closest to the end of the alphabet.
    except FileNotFoundError: #File not found
        print(f"ERROR:: '{fileName}' not found.")
    except Exception as e: #Unexpected error
        print(f"An error occurred: {e}")

def isNumber(word):
    try:
        float(word)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: challenge6.py filename")
    else:
        fileName = sys.argv[1]
        letterFilter(fileName)