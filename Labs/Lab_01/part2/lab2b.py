''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 1 part 2 Question 3 (lab2b.py).  
''' 


gross_income = input("Enter your gross income:")        #get gross income as user input
dependents = input("Enter the number of dependents:")   #get dependents as user input 
standerd_deduction = 10000                              #defined standerd deduction
dependent_deduction = 2000 * int(dependents)            #calculate deduction due to number of dependents
taxable_income = int(gross_income) - standerd_deduction - dependent_deduction #calculate taxable income
income_tax = 0  #defined income tax

#Calculate incometax - start
if int(gross_income) < 32000:
    income_tax = taxable_income * 0.1
elif 32000 <= int(gross_income) < 64000:
    income_tax = taxable_income * 0.15
else:
    income_tax = taxable_income * 0.25

if income_tax < 0:
    income_tax = 0
#Calculate incometax - end

print("The income tax is $"+str(round(income_tax))+".")     #final output