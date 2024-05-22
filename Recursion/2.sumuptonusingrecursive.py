def factorial(s):
    if s==0:
        return 0
    return s+factorial(s-1) 

s = int(input())
print(factorial(s))