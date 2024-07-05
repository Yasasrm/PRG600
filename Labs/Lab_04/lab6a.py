''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 4 Question 1 (lab6a.py).  
''' 

data_to_write = ['First Line!', 'Second Line!!', 'Third Line!!!', '...and so on!']

f = open('testing.txt', 'w')  #Create a file object
for line in data_to_write:    #Get next line
    f.write(line + '\n')      #Write next line
f.close()                     #Close file object