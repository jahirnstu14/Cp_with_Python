import math
x = float(input("Enter the value of x in radians : "))
n = int(input("Enter the value of n : "))

cos_apprx = 0.0
term=0

for k in range(n+1):
    term = (-1)**k * (x**(2*k)) / math.factorial(2*k)
    cos_apprx+=term
print(f"Macline series value is {cos_apprx}")