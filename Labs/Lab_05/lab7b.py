''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 5 Question 2 (lab7b.py).  
''' 

#Meal plan details
meal_plan = {'breakfast': 'oatmeal', 'lunch': 'sandwiches', 'dinner': 'broccoli'}

#Print meal plan using f string
def print_meal_plan(mealPlan):
    print(f"{'MENU FOR TODAY': ^50}")
    print(f"{'='*50: ^50}")
    print(f"{'Breakfast' : <25}{mealPlan['breakfast'] : >25}")
    print(f"{'Lunch' : <25}{mealPlan['lunch'] : >25}")
    print(f"{'Dinner' : <25}{mealPlan['dinner'] : >25}")

if __name__ == "__main__":
    print_meal_plan(meal_plan)