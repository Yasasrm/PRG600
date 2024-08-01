''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 6 part 1 Question 1 (lab8a.py).  
''' 

import re 
 
tel_num = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
mo = tel_num.search('My telephone number is 555-877-5678. Or you can reach me on my cell: 555-212-0771. Call me!') 
print('Found phone number: ' + mo.group()) 