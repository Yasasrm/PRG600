''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 2 Question 2 (lab4b.py).  
''' 

from random import randint 

def rtrn_area(length, width): # Parameters- Length, Width | Returns- Area 
    '''When given length and width, area will be calculated''' 
    return length * width 

rect = rtrn_area(4, 3) # call the function again with new values
print(rect) 

def print_all_caps(name, age): # Parameters- Name, Age | Returns- Nothing  
    '''When given name and age, caption will be printed, name will be converted to all capital'''
    cap_name = name.upper() 
    print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age) + ' YEARS OLD!!!')
    return

print_all_caps('yasas', 30) 
print_all_caps('ron', 40) # call the function again with new values 
    
def get_rando(): # Parameters- Nothing | Returns- Nothing  
    '''generate a random number between 1 - 101'''
    return randint(1, 101) 

lucky_num = get_rando() # call the function again with new values 
print(lucky_num)

def is_odd(num): # Parameters- Number(num) | Returns- Boolean  
    '''Check whether the number odd or even''' 
    if num % 2 == 1: 
        return True 
    else: 
        return False 
    
print(is_odd(13)) 
print(is_odd(get_rando())) # call the function again with new values