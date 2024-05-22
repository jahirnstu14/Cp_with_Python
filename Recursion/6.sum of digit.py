def sumofdigit(n):
    if n==0:
        return 0
    return sumofdigit(n//10)+n%10

    
n = int(input())
print(sumofdigit(n))


# the number of function call  = number of digit (logn)
# each function complexity