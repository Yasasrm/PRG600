''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 5 Question 3 (lab7c.py).  
''' 

from lab7b import print_meal_plan

template = {'breakfast': None, 'lunch': None, 'dinner': None}
days = []

def bookDates():
    while True:
        needToAddNewDate = input("Would you like to add a day? (y/n) ").strip().lower()
        if needToAddNewDate == 'n':
            break
        elif needToAddNewDate == 'y':
            new_day = template.copy()
            for meal in new_day.keys():
                new_day[meal] = input(f"Please enter what you would like to eat for {meal}: ").strip()
            days.append(new_day)
        else:
            print("Invalid input, please enter 'y' or 'n'.")

def printDate():
    if not days:
        print("No days added. Exiting program.")
    else:
        while True:
            try:
                dayNumber = int(input(f"Please enter a day number for the menu you would like to print (1-{len(days)}): "))
                if 1 <= dayNumber <= len(days):
                    print_meal_plan(days[dayNumber - 1])
                    break
                else:
                    print(f"Error: Number out of range. Date should be between 1 and {len(days)}.")
                    break
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    bookDates()
    printDate()
