def factorial(s):
    if s==0:
        return 1
    return s*factorial(s-1) 

s = int(input("Enter number:"))
print(factorial(s))