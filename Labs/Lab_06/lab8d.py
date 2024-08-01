''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 6 part 1 Question 4 (lab8d.py).  
''' 

import os 
 
course_dir = '..' 
 
print('Your current directory is: ' + os.path.abspath(course_dir)) 
for root, directories, filenames in os.walk(course_dir): 
    for file in filenames: 
        print(os.path.join(root, file))