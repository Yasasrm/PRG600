''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 3 Question 1 (lab5a.py).  
''' 

def my_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum



if __name__ == "__main__": 
    user_numbers = [] 
    print("AVERAGE CALCULATOR") 
    while True: 
        user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") 
        if user_input == "": 
            break 
        else:  
            user_numbers.append(int(user_input)) 
    num_sum = my_sum(user_numbers) 
    num_length = len(user_numbers) 
    average = num_sum / num_length 
    print(f"Total sum is: {num_sum}. Total count is: {num_length}. Average for this list is: {average}.") 
    print("Thank you for using average calculator.")