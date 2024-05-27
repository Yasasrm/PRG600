''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 2 part 2 Question 2 (lab4b.py).  
''' 

from random import randint 

def rtrn_area(length, width): # Put your in-line comment here 
    "Put your function level docstring here" 
    return length * width 

rect = rtrn_area(5, 3) # call the function again with new values 

def print_all_caps(name, age): # Put your in-line comment here 
    '''Put your function level docstring here'''
    cap_name = name.upper() 
    print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age) + ' YEARS OLD!!!')
    return

print_all_caps('eric', 41) 
print_all_caps('melissa', 40) # call the function again with new values 
    
def get_rando(): # Put your in-line comment here 
    '''Put your function level docstring here'''
    return randint(1, 101) 

lucky_num = get_rando() # call the function again with new values 

def is_odd(num): # Put your in-line comment here 
    '''Put your function level docstring here''' 
    if num % 2 == 1: 
        return True 
    else: 
        return False 
    
print(is_odd(13)) 
print(is_odd(get_rando())) # call the function again with new values