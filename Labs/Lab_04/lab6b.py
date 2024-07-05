''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 4 Question 2 (lab6b.py).  
''' 

import sys

def reverseFilePrinter(fileName):
    f = open(fileName, 'r')  #Create a file object
    content = f.readlines()  #Load file content
    f.close()                #Close file object
    content.reverse()        #Reverse file content
    for line in content:     #Print content
        print(line.strip())

if __name__ == "__main__":
    fileName = 'readme.txt' if len(sys.argv) == 1 else sys.argv[1] # Use 'readme.txt' if no command line argument is provided
    reverseFilePrinter(fileName)