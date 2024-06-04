''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 3 Question 3 (lab5c.py).  
''' 

import random

animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel', 'vulture', 'horse', 'python', 'capybara' ]
secret = random.randint(0, len(animals)-1)

while True:
    print("I'm thinking of an animal. Can you guess what it is?")
    guess = input("Enter a letter or a guess. Press enter to quit:")
    if guess == "":
        break
    elif len(guess) >1 and guess == animals[secret]:
        print("You win!")
    elif len(guess) == 1 and guess in animals[secret]:
        print("Yes, my word contains that letter.")
    elif len(guess) == 1:
        print("Sorry, my word doesn't contain that letter.")
    else:
        print("Sorry, that's not it.")