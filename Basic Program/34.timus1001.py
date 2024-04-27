from math import sqrt

number = input("Enter the number with space : ").split()

for i in reversed(number):
    k=sqrt(float(i))
    print(f" The sqrt root of the number is {k:.4f}")