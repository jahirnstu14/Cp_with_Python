# For number factorization , the smallest divisor of the number is prime number . example :  36  = 2^2 * 3^2 . here smallest divisor is 2 . so , 2 is prime number . for 91 = 7*13 . so, 7 is prime number. 

# firstly we start divisor from smallest prime number. example : 36/2=18,18/2=9, 9/3=3, 3/3 =1, here , 36 has smallest divisor 2, 18 has smallest divior 2, 9 has smallest divisor is 3, 3 has smallest divisor is 1

# n = int(input())

# prime_factorization = []

# for i in range(2,n):
#     while n%i==0:
#         prime_factorization.append(i)  # time complexity is 0(n)
#         n//=i

# print(prime_factorization)


# any composite number or not prime number, must have one divisor less or equal to sqrt(compostie number)which is number  . like example : if we consider 
# 36 =1 * 36
#     2 * 18
#     4 * 9
#     6 * 6
#     9 * 4
#     18 * 2
#     36 * 1

# the sqrt(36) = 6 , so, there is at least one  prime number below 6 or 6  that is used to divide the composite number . 
# in bangla simply : কোন কম্পোজিট নম্বর এর জন্য মিনিমাম একটা prime divisors অবশ্যই  থাকবে যেটা composite সংখ্যার বর্গমূলের সমান ba ওর ছোট হবে . principal theorem. first check start from 2 upto  sqrt(n)

import math
n = int(input())

prime_factorization = []
sqrt_n = int(math.sqrt(n)) + 1

for i in range(2,sqrt_n):
    while n%i==0:
        prime_factorization.append(i)  # complexit will be : 0(N*sqrt(N))
        n//=i
        
if n>1:
    prime_factorization.append(n) # for 1337 loop will be executed in one time . so, 191, then it will be executed n>1 condition .or for prime number

print(prime_factorization)



 

