import math
a = int(input("Enter the length of one arms of triangle :"))
b = int(input("Enter the length of one arms of triangle  :"))
c = int(input("Enter the length of one arms of triangle  :"))
def findArea(a,b,c):
    half_circumference = (a+b+c)/2
    area = math.sqrt(half_circumference*(half_circumference-a)*(half_circumference-b)*(half_circumference-c))
    return area
    
Area = findArea(a,b,c)
print(f"the Area of triangle will be :{Area}")