''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 4 Question 4 (lab6d.py).  
''' 

import sys

def letterFilter(fileName):
    try:
        f = open(fileName, 'r')  #Create a file object (read)
        content = f.readlines()  #Load file content
        f.close() #Close file object
        for _, line in enumerate(content):
            print(sum([float(word) for word in line.split() if isNumber(word)])) #Print sum of the numbers in the line
        f = open(fileName, 'w')  #Create a file object (write)
        for _, line in enumerate(content):
            f.write((" ".join(word for word in line.split() if not isNumber(word)) + '\n')) #Write letters to the file
        f.close() #Close file object
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
        print("Usage: lab6c.py filename")
    else:
        fileName = sys.argv[1]
        letterFilter(fileName)