''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 6 part 1 Question 2 (lab8b.py).  
''' 

import sys
import re


def getPhoneNumbers(filename):
    # Attempt to open the file and read its contents
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    # Define the regex pattern for phone numbers
    phonePattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    
    # Use findall to match all phone numbers in the content
    return re.findall(phonePattern, content)

if __name__ == "__main__":

    # Check if filename is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python lab8b.py <filename>")
        sys.exit(1)

    # Read file and get phone numbers  
    phoneNumbers = getPhoneNumbers(sys.argv[1])
    
    # Print the number of results found
    print(f"Found {len(phoneNumbers)} phone number(s).")
    
    # Ask the user if they want to see the results
    userInput = input("Would you like to see the results? (y/n): ").strip().lower()
    
    if userInput in ['y', '']:
        for number in phoneNumbers:
            print(number)
    elif userInput == 'n':
        sys.exit(0)
    else:
        print("Invalid input. No results will be shown.")
