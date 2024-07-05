''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 5 Question 1 (lab7a.py).  
''' 

student1 = ['eric', 'smith', '217 Au Large Blvd', 'Toronto', 'Ontario', 'M4A 1P3']

def shipping_label(a_lst): 
    "takes a list, generates a string" 
    a_str = f"{a_lst[0]} {a_lst[1]}\n" 
    a_str += f"{a_lst[2]}\n" 
    a_str += f"{a_lst[3]}, {a_lst[4]}\n"
    a_str += f"{a_lst[5]}" 
    return a_str

if __name__ == "__main__":
    print(shipping_label(student1))