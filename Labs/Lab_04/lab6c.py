''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 4 Question 3 (lab6c.py).  
''' 

import sys

def search(keyword, fileName):
    try:
        f = open(fileName, 'r')  #Create a file object
        content = f.readlines()  #Load file content
        f.close()                #Close file object
        for lineNumber, line in enumerate(content, start=1): #Searching for keyword
            if keyword in line:                     #Keyword found
                print(f"{lineNumber}: {line.strip()}")
    except FileNotFoundError: #File not found
        print(f"ERROR:: '{fileName}' not found.")
    except Exception as e: #Unexpected error
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: lab6c.py keyword filename")
    else:
        keyword = sys.argv[1]
        fileName = sys.argv[2]
        search(keyword, fileName)
