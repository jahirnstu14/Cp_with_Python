x1 = float(input("Enter the first coordinates first number :"))
y1 = float(input("Enter the first coordinates second number :"))
x2 = float(input("Enter the second coordinates first number :"))
y2 = float(input("Enter the second coordinates first number :"))

Distance_between_two_point =int(abs(((x2-x1)**2 + (y2-y1)**2)**0.5))
print (f"Distance_between_two_point is : {Distance_between_two_point}")
