import math
x1,y1=map(float,input("Enter the coordinates point in two dimensional coordinates(x1 y1):").split())
x2,y2=map(float,input("Enter the coordinates point in two dimensional coordinates(x2 y2):").split())
x3,y3=map(float,input("Enter the coordinates point in two dimensional coordinates(x3 y3) :").split())

Area_of_triangle = 0.5 *abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
print(Area_of_triangle)