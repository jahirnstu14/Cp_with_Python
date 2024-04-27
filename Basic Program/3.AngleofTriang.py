import math
a = int(input("Enter the length of one arms of triangle :"))
b = int(input("Enter the length of one arms of triangle  :"))
c = int(input("Enter the length of one arms of triangle  :"))
def findangle(a,b,c):
    angleA = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
    angleB = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
    angleC = math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a)))
    return angleA , angleB ,angleC
# converting radian to degree 
# AngleA= angleA* 180 / math.pi; 
# AngleB= AngleB * 180 / math.pi; 
# AngleC = AngleC * 180 / math.pi; 
    
angles =findangle(a,b,c)
print (f"the angle A is  : {angles[0]} ,the angle B is :{angles[1]} , the angle C  is :{angles[2]}")

