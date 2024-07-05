''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 5 Question 1 (lab7a.py).  
''' 

student1 = {'first_name': 'eric', 'last_name':'smith', 'addr1': '217 Au Large Blvd', 'city': 'Toronto', 'prov': 'Ontario', 'pcode': 'M4A 1P3'}

def shipping_label(a_lst): 
    "takes a list, generates a string" 
    a_str = f"{a_lst['first_name']} {a_lst['last_name']}\n".upper() 
    a_str += f"{a_lst['addr1']}\n" 
    a_str += f"{a_lst['city']}, {a_lst['prov']}\n"
    a_str += f"{a_lst['pcode']}" 
    return a_str

if __name__ == "__main__":
    print(shipping_label(student1))