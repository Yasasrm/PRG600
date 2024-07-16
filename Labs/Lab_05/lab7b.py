''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 5 Question 2 (lab7b.py).  
''' 

meal_plan = {'breakfast': 'oatmeal', 'lunch': 'sandwiches', 'dinner': 'broccoli'}

def print_meal_plan(mealPlan):
    print("MENU FOR TODAY\n==============")
    print(mealPlan['breakfast'])
    print(mealPlan['lunch'])
    print(mealPlan['dinner'])

if __name__ == "__main__":
    print_meal_plan(meal_plan)