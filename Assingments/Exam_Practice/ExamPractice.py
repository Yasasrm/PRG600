''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
''' 

# Question 1

# Write a program to remove the item present at 

# index 4 and add it to the 2nd position and at the end of the list.

# list1 = [54, 44, 27, 79, 91, 41]

def question1():
 list1 = [54, 44, 27, 79, 91, 41]
 item = list1.pop(4)
 list1.insert(2, item)
 list1.append(item)
 print(list1)
 pass



# Question 2

# Given a two Python list. 

# Write a program to iterate both lists simultaneously 

# and display items from list1 in original order and items from list2 in reverse order.

# list1 = [10, 20, 30, 40]

# list2 = [100, 200, 300, 400]

def question2():
 list1 = [10, 20, 30, 40]
 list2 = [100, 200, 300, 400]
 length = len(list1)
 
 for i in range(length):
    print(list1[i], list2[(length - 1) - i])
pass



# Question 3

# write a function that takes a row count and print a pyramid like this

# 1 

# 2 2 

# 3 3 3 

# 4 4 4 4 

# 5 5 5 5 5

# The above pyramid is 5 rows.

def question3():
    rows = 5
    for i in range(1, rows + 1):
       print((str(i) + ' ') * i)
    pass



if __name__ == '__main__':
  print("Running Question 1")
  question1()
  print("")
  print("Running Question 2")
  question2()
  print("")
  print("Running Question 3")
  question3()