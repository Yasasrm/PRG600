''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 3 Question 3 (lab5c.py).  
''' 

import random

animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel', 'vulture', 'horse', 'python', 'capybara' ]
secret = random.choice(animals)  # Choose a random animal from the list as the secret word

while True:
    
    print("I'm thinking of an animal. Can you guess what it is?")
    guess = input("Enter a letter or a guess. Press enter to quit:") #user input (guess)

    if guess == "": #exit the loop
        break
    elif len(guess) >1 and guess == secret: #guess correct word
        print("You win!")
        break
    elif len(guess) == 1 and guess in secret: #guess a letter contain in the secret
        print("Yes, my word contains that letter.")
    elif len(guess) == 1:  #guess a letter not contain in the secret
        print("Sorry, my word doesn't contain that letter.")
    else:  #guess a wrong word
        print("Sorry, that's not it.")