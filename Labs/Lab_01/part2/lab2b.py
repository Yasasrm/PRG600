''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 1 part 2 Question 3 (lab2b.py).  
''' 

gross_income = input("Enter your gross income:") 
dependents = input("Enter the number of dependents:") 
standerd_deduction = 10000
dependent_deduction = 2000 * int(dependents)
taxable_income = int(gross_income) - standerd_deduction - dependent_deduction
income_tax = 0

if taxable_income < 32000:
    income_tax = taxable_income * 0.1
elif 32000 <= taxable_income <= 64000:
    income_tax = taxable_income * 0.15
else:
    income_tax = taxable_income * 0.25

if income_tax < 0:
    income_tax = 0

print("The income tax is $"+str(round(income_tax))+".") 
