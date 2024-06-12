# find the divisor of a number 
# first time 

# n = int(input("Enter the number to find the divisor : "))

# for i in range(1,n+1):
#     if n%i==0:             # time complexity for above program 0(n)
#         print(i,end=" ")
        

# 2nd time 

# n = int(input("Enter the number to find the divisor : "))

# count = 0
# sum = 0

# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")   # time complexity for above program 0(n)
#         count+=1
#         sum+=i
#         if n/i==i:
#             count-=1

# print()        
# print(f"the number of divisor of {n} is {count} and divisor sum is {sum}")


# 3rd time 
import math
n = int(input("Enter the number to find the divisor : "))

count = 0
sum = 0

sqrtroot = math.sqrt(n) + 1
sqrtroot = int(sqrtroot)

for i in range(1,sqrtroot):   #using while loop : i*i <=n
    if n%i==0:
        print(f"{i} {n//i}")   # time complexity for above program 0(sqrt(n))
        count+=1
        sum+=i
        if n/i!=i:
            sum+=n//i
            count+=1
       
print(f"the number of divisor of {n} is {count} and divisor sum is {sum}")


# some basic of divisor 

# factoriziation of x :

# x = p1^n1 * p2^n2 * p3^n3 where p1,p2,p3 are prime number .
# the number of divisor = (n1+1)*(n2+1)*(n3+1)
# example : 36 = (2+1)*(2+1)   where, 36 = 2^2 * 3^2

# some of divisor = (1+p1+p1^2+p1^3...+p1^n) * ((1+p2+p2^2+p2^3...+p2^n)) * (1+p3+p3^2+p3^3...+p3^n)
                
#                 =((p1^(n1+1) + 1)/(p1-1)) * ((p2^(n2+1) + 1)/(p2-1)) * ((p3^(n3+1) + 1)/(p3-1)) 

# If you have two positive numbers N AND D, such that N is divisible by D and D is less than the squre root of N. (N/D) must be greater than the square root of N . example : N =12, sqrt(12) . if we divide  by 3 which is smaller than sqrt(N) .THEN 12/3 =4,WHICH IS GREATER THAN SQRT(12).      

        
    
    