''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 3 Question 5 (challenge5.py).  
''' 

import random

vehicle_brands = [
    "Toyota",
    "Ford",
    "Honda",
    "Chevrolet",
    "Mercedes-Benz",
    "BMW",
    "Audi",
    "Volkswagen",
    "Nissan",
    "Hyundai",
    "Kia",
    "Lexus",
    "Subaru",
    "Mazda",
    "Jeep",
    "Dodge",
    "Ram",
    "Tesla",
    "Volvo",
    "Jaguar",
    "Porsche",
    "Land Rover",
    "Fiat",
    "Mitsubishi",
    "Mini",
    "Buick",
    "Cadillac",
    "GMC",
    "Acura",
    "Infiniti",
    "Lincoln",
    "Chrysler",
    "Alfa Romeo",
    "Peugeot",
    "Renault",
    "Citroën",
    "Skoda",
    "Seat",
    "Saab",
    "Suzuki",
    "Maserati",
    "Ferrari",
    "Lamborghini",
    "Bentley",
    "Rolls-Royce",
    "Aston Martin",
    "Bugatti",
    "McLaren",
    "Genesis"
]



def  getEmptyList(length): #returns a list of underscores with the length of the secret
    return ["_" for _ in range(length)]

def fillGuessingWord(word, secret, char): #replace undescore with correct character
    i = 0
    for character in secret:
        if character == char and  word[i] == "_":
            word[i] = char
            break
        else:
            i += 1

def printGuessingWord(word): #print list of guesses as a single string, characters are sepereted by space
    print(" ".join(word))

if __name__ == "__main__":  #entry point
    secret = random.choice(vehicle_brands).lower()
    print("I'm thinking of a vehicle brands. Can you guess what it is?")
    word = getEmptyList(len(secret))
    while True:
        print("Your word:")
        printGuessingWord(word)
        guess = input("Enter your guess:").lower() #user input (guess)
        if guess == "":   #exit the loop
            break
        elif len(guess) >1 and guess == secret: #guess correct word
            print("You win!")
            break
        elif len(guess) == 1 and guess in secret: #guess a letter contain in the secret
            fillGuessingWord(word, secret, guess)
            printGuessingWord(word)
        elif len(guess) == 1: #guess a letter not contain in the secret
            print("Sorry, my word doesn't contain that letter.")
        else:
            print("Sorry, that's not it.") #guess a wrong word


