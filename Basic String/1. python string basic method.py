# # dict types or mapping types
# person = {
#     "first_name " : "Jahirul",   # key and value pair
#     "last_name " : "lslam",
#     "age" : 25,
#     "isbangladeshi" : True
# }
#
# print("name:",person["first_name "], "last_name:",person["last_name "],"age:",person["age"],"isbangladeshi:", person["isbangladeshi"])

# in python , third bracket or square brackets represent list  -> mutable -> changable
            # first bracked or first parenthesis represent tuple --> immutable -> unchangeable
            # second bracket or curly bracket represent set -->>mutable and forzenset --> immutable
'''
numberset = {1,2,3,4,5,5}
print(numberset)

numberset = frozenset([1,2,3,4,5,5])
print(numberset)
'''

# Immutable :
# immutable cannot be modified after their creation
# - integer
# - Floating point numbers
# - String
# - Tuples
# - Frozenset()

# a = 5
# first_location = id(a) # id function is used to find variable location
# a = 6
# second_location = id(a)
# print(first_location)
# print(second_location)
#
# from above we can see that first and second location are different though the variable name is same. যেহেতু লোকেশান পরিবর্তন হইছে
# তাই আমারা বলতে পারি একি ভারিয়াব্লেকে পরিবর্তন করা সাম্বভ নয় . for this it is called immutalbe .

# for string :
# a = "ami"
# first_location = id(a)  # id function is used to find variable location
# a = "tumi"
# second_location = id(a)
# print(first_location)
# print(second_location)

# similarly for other thing

# mutable datatype :
# list
# dictionaries
# set()
#
# for list :
# list1 = [1,2,3]
# first_location = id(list1)
# print(first_location)
# list1[2]=9
# second_location = id(list1)
# print(second_location)
#
# as they have same location so, they are mutable .

# for dictionaries :
# dict1 = {'a': 1,'b': 2}
# first_location = id(dict1)
# print(first_location)
# dict1['a'] = 4
# second_location = id(dict1)
# print(second_location)
# as they have same location so, they are mutable .
#
# type conversion -
# 1. explicit conversion - forcely conversion - example->int(),float()etc
# 2. implicit conversion - automatic conversion - example -> x=3,y=3.22, here implicitly x asigned int and y asigned float

# positive slicing
# text1 = "Helloworld"
# text2 = "amiami"
# # # step : 2
# # print(  )
# # print(text2[::-1])
# print(text2[1::3])

# for slicing first will be starting point, second will be stop with exclusive and thirt 2 is skip .

# string repettion

# name = "shanto "
# print(10 * name)

# string concatenation
# using +
# str1 ="hellow"
# str2 = "world"
# combine = str1 + " : " + str2 + "!"
# print(combine)

# using join method
# str1 ="hellow"
# str2 = "world"
# combine = ",".join([str1,str2]) + "!"
# print(combine)
# format method
# str1 ="hellow"
# str2 = "world"
# combine = "{} {} ".format(str1,str2)
# print(combine)

# using % signature
# str1 ="hellow"
# str2 = "world"
# combine = "%s %s" %(str1,str2)
# print(combine)

# different string method
# convert to uppercase
# text = "hellow world"
# print(text.upper())
#
# # convert to uppercase
# text = "HELLOW WORLD"
# print(text.lower())
#
# # first character capitalize
# text = "hellow world"
# print(text.capitalize())
#
# # every word first letter capital or tilte
# text = "hellow world "
# print(text.title())
#
# text = "HelloW world"
# print(text.swapcase())
#
# # string replace
# text = "hellow world"
# print(text.replace("world","python"))
#
# # split the string
# text = "hellow-world-with-python"
# print(text.split("-")) # means text convert into list using delimiter
#
# # join the list element to convert string
#
# text = ['hellow', 'world', 'with', 'python']
# print(",".join(text))
#
# # strip whitespace starting and ending
#
# text = " hello world "
# print(text.strip())
#
# # remove leading whitespace
# text = " hello world "
# print(text.lstrip())
#
# # remove trailing whitespace
# text = " hello world "
# print(text.rstrip())

# # if check string startwith with a substring
# text = "hellow world"
# print(text.startswith("hellow"))
# # if check string endwith with a substring
# text = "hellow world"
# print(text.endswith("world"))
#
# # find the position of substring from where substring has been started
# text = "hellowworld"
# print(text.find("world"))

# count occurence of substring
# text = "hellow world"
# print(text.count("l"))

# # check if all character alphanumearic
# text = "hellow world"
# print(text.isalnum())
#
# # check if all character alphabetic or not
# text = "hellowworld"
# print(text.isalnum())
#
# # check if all character digit or not
# text = "hellow world"
# print(text.isnumeric())
#
# # check if only whitespace
# text = "      "
# print(text.isspace())
#
# # check if title case kina string
# text = "Hellow World"
# print(text.istitle())

# # capitalizing each word of sentence
# text = "i am a student of noakhali science and technology university "
# print(text.title())
#
# # Removing extra space and converting to uppercase
# text = " i am a student of noakhali science and technology university  "
# print(text.strip().upper())

# math built in function in python
# square root of a number
# import math
# num = 16
# print(math.sqrt(num))
#
# # square root of a number
# from math import sqrt
# num = 16
# print(sqrt(num))
#
# # power of a number 4^2
# from math import pow
# num = 16
# print(pow(4,2))
#
# # trigonometrics function
# from math import sin
# print(math.sin(math.radians(90)))

# logarithmeic function
# import math
# print(math.log10(10))
#
# # factorial of a number
# print(math.factorial(5))
#
# # absolute value
# print(math.fabs(-9))
# # floor and ceiling function
# print(math.floor(3.7))
# print(math.ceil(3.7))
#
# # constant value
# print(math.pi)
# print(math.e)
#
# # gcd and lcm
# print(math.gcd(6,12))
# print(math.lcm(6,12))

text = "helloworld!"
print(text[-3:])


































































