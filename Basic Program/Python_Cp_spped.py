# 1. Use the proper algorithm and data structure 
# 2.there many build in data structure such as list , tuple,set and dictionary 
# 3.Most use List data structure and sets and dictionaries has 0(1) time complexity.
# 4.link for : data stucture complexity :https://wiki.python.org/moin/TimeComplexity
# 5.Using python built in function which writen by c such as 
#   min,max,all,map ,avg
  
  
# low speed : newlist = []
#            for word in wordlist:
#                newlist.append(word.upper())
                
# alternative for high speed  : newlist = map(str.upper, wordlist) where map function writen in case

# low spped : firstName ="Name"
#             lastName ="Henry"
#             city     ="Manchester "
# alternative for high speed  : firstName,lastname,city = "Name","Henry","Manchester"

# Prefer list comprehension over loops 
# low speed  : newlist = []
#              for i in range(1,100):
#                  if i%2 ==0:
#                      newlist.append(i**2)
                     
# alternative for high speed :
#     newlist = [i**2 for i in range(1,100)if i%2==0]

# proper import

# for lower speed : import math 
#                   value = math.sqrt(50)
# for high speed : from math import sqrt 
#                  value = sqrt(50)

# string concatenation :
#     lower speed : output = "Programmng"+"is"+"fun"
    
#     higher speed : output = " ".join(["Programming", "is","fun"])
# Tuple has more speed than list 

# As for loop is dynamic in python, it takes more time than while loop. So, use while loop instead of for loop.
# Do not use global variables because , global variaable takes high times 

# for low speed : l = []
#                 for element in set(l):
# for high speed : for element in l :
    
# donot use dot operation 
# example : for low speed : import math
#            val = math.sqrt(60)
# for high speed : from math import sqrt
#                    val = sqrt(60)
                   
# Use while 1 instead of while True 

# Try different approach :
# low speed :
# if a_condition:
#     if another_condition:
#         do_something
# else:
#     raise exception
    
# high speed :
# if (not a_condition) or (not another_condition):
#     raise exception
# do_something   

# Pypy and Numba two of them. In most of the programming contests, you will see pypy if it allows python

# If you don’t have duplicate items in the collection, you need to search items repeatedly and 
# the collection contains a large number of items, then using sets and dictionaries would be the wise decision than 
# using lists. Sets and dictionaries use hash tables, so, the time complexity of each lookup is only O(1).

# low speed :
#  from math import sqrt
	

# mylist  = [5, 3, 45, 49]
# newlist = []
	

# for x in mylist:
#     newlist.append(sqrt(x))
    
# high spped:
# from math import sqrt
# mylist = [5, 3, 45, 49]
# newlist = map(sqrt, mylist)  

# use list compresiong : low speed:
# mylist = []
	

# for i in range(1, 21):
#     for j in range(1, 21):
#         if i % 3 == 0 and j % 5 == 0:
#             mylist.append((i, j))
            

# for high speed : 
#     mylist = [(i,j) for i in range(1,21) for j in range(1, 21) if i%3==0 and j%5==0]

# for low speed :
#     if condition_a:
#         if condition_b:
#             if condition_c:
#                 do_something
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False

# high speed :
# if (not condition_a) or (not condition_b) or (not condition_c):
#     return False
# do_something
# return True

# for input high speed :
# import sys
# reading a single integer 
# n = int(sys.stdin.readline())
#  reading a list on intergeres
# arr = list(map(int , sys.stdin.readline().spilt()))

# for high speed output buffering  remove  :
# import sys
# print("output")
# sys.stdout.flush()
# always use sys.stdout.flush() after each print statement 

# for taking high speed integer list :
# import sys
# # Reading a list of integers
# arr = [int(x) for x in sys.stdin.readline().split()] 

# for string input with high speed :
# import sys

# # Using sys.stdin to read a line as a string
# input_string = sys.stdin.readline().rstrip()


import sys
# n = int(sys.stdin.readline())
n = [int(x) for x in sys.stdin.readline().split()] 
print(f"good to see you")


sys.stdout.flush()

    
            
            
   
     








