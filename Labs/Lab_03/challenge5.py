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



def  getEmptyList(length):
    emptyString = []
    while length > 0:
        emptyString.append("_")
        length -= 1
    return emptyString

def fillGuessingWord(word, secret, char):
    i = 0
    for character in secret:
        if character == char and  word[i] == "_":
            word[i] = char
            break
        else:
            i += 1

def printGuessingWord(word):
    printString = ""
    for character in word:
        printString += character+" "
    print(printString.strip())

if __name__ == "__main__":
    secret = random.choice(vehicle_brands).lower()
    print("I'm thinking of a vehicle brands. Can you guess what it is?")
    word = getEmptyList(len(secret))
    while True:
        print("Your word:")
        printGuessingWord(word)
        guess = input("Enter your guess:")
        if guess == "":
            break
        elif len(guess) >1 and guess == secret:
            print("You win!")
            break
        elif len(guess) == 1 and guess in secret:
            fillGuessingWord(word, secret, guess)
            printGuessingWord(word)
        elif len(guess) == 1:
            print("Sorry, my word doesn't contain that letter.")
        else:
            print("Sorry, that's not it.")


