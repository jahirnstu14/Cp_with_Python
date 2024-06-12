# n = int(input())

# is_prime = True

# for i in range(2,n):
#     if n%i==0:
#         is_prime = False  # the time complexity for this problem is 0(n)
#         break

# if is_prime:
#     print(f"{n} is prime number ")
# else:
#     print(f"{n} is not prime number ")



# second method for decreasing the program complexit of sqrt(n):
import math
n = int(input())

is_prime = True
sqrt_n = int(math.sqrt(n))+1

if n==1:
    print("{n} is not prime number ")
    
else:
    for i in range(2,sqrt_n):
        if n%i==0:
            is_prime = False  # the time complexity for this problem is 0(sqrt(n))
            break

    if is_prime:
        print(f"{n} is prime number ")
    else:
        print(f"{n} is not prime number ")    



