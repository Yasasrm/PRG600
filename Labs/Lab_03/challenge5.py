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

secret = random.randint(0, len(vehicle_brands)-1)

while True:
    print("I'm thinking of a vehicle brands. Can you guess what it is?")
    guess = input("Enter a letter or a guess. Press enter to quit:")
    if guess == "":
        break
    elif len(guess) >1 and guess == vehicle_brands[secret]:
        print("You win!")
    elif len(guess) == 1 and guess in vehicle_brands[secret]:
        print("Yes, my word contains that letter.")
    elif len(guess) == 1:
        print("Sorry, my word doesn't contain that letter.")
    else:
        print("Sorry, that's not it.")