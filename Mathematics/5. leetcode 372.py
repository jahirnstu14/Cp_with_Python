# https://leetcode.com/problems/super-pow/

# power of power rule :  (a^b)^c = a^(b*c)

# same euler theorem in different way :
# This program is based on Euler's Theorem which states that: a^( phi(n) ) = 1 (mod n), where phi(n) is Euler's Totient Function, provided that a and n are relatively prime (meaning they have no common factors). In our case, n = 1337, which has prime factorization 1337 = 7 x 191. We know that phi(p) = p - 1 when p is prime and also that phi(p x q) = phi(p) x phi(q). Thus it follows that phi(1337) = phi(7 x 191) = phi(7) x phi(191) = 6 x 190 = 1140. 

# shortcut solution using pow python default function 

# base = int(input("Enter the base : "))
# p = list(map(str,input("Enter the array for power : ").split()))

# mode = 1337
# power =""

# for i in p:
#     power+=i
# power = int(power)

# print(pow(base,power,mode))


# below program solution logic : 

# This is a simple approach to the problem Super Pow.This requires few concepts of mathematics which are Euler's theorem and ETF(Euler Totient Function).
# Now,what is ETF ?
# ETF of a number n can be defined as :

# ETF(n)=n*product_of(1-1/p)
# where p=prime factors.
# Euler's Theorem States that:
# a^b %M =a^(b%ETF(n)) % M .
# In This question ETF(1337)=1140.
#  if a has neither divisor 7 nor 191, that's a and 1337 are coprime, so a^b % 1337 = a^b % phi(1337) % 1337 = a^b % 1140 % 1337.

def binary_exponenet(base,power):
    base%=1337
    ans = 1
    while power>0:
        if power&1:
            ans = (ans * base) % 1337      # the complexity of this function is logb(b number of bits in binary of power )
        base = (base * base)% 1337
        power>>=1
    return ans 

    
a = int(input("Enter the base : "))
b = list(map(int,input("Enter the array for power : ").split()))

# ETF(1337) = 1140
sum = 0

for i in range(len(b)):
    sum = ((sum * 10)+b[i]) % 1140
    
if sum == 0:
    sum = 1140
print(binary_exponenet(a,sum))
    




















    