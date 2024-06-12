# # Modular multiplicative inverse

# link to know inverse modular multipication : https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/

# we know, A * B =1 ,
# The value of B is 1/A or A-1 . HERE , B is the multiplicative inverse of A. 
# similarly , (A * B) % M =1,
# HERE, B is the multipicative inverse of A under mmoudlo M. 

# and we also can say that A * B = 1(MOD M) where B is the range of [1,M-1]
 
#  second approach : A and M are coprime i.e. Ax + By =1 
# . In the extended Euclidean algorithm, x is the modular multiplicative inverse of A under modulo M. Therefore, the answer is x. You can use the extended Euclidean algorithm to find the multiplicative inverse.

# For example, if A=5 and M=12, then GCD(A,B)=1
# . Therefore, the inverse exists.

# 3rd approach: (used only when M is prime ):
# the theorem specifies that A^(M-1) = 1 (MOD M).  This approach uses Fermat's Little Theorem.
# By multiplying with A-1
#  both sides,the equation can be rewritten as follows:

# A-1 = A^(M-2) MOD M 
M = int(1e5+10)

def binary_exponenet(base,power,M):
    ans = 1
    while power>0:
        if power&1:
            ans = (ans * base) % M      # the complexity of this function is logb(b number of bits in binary of power )
        base = (base * base)% M
        power>>=1
    return ans  

# to find modular inverse, we can write a 
# a = int(input())
# a=2
# print(binary_exponenet(2,M-2,M))

# question : 
# There are N children  and K toffees . K<N 
# count the number of ways to distribute toffee
# among the N students.such that each students get 1 toffee only -> solution : nCK % M, M =10^9 + 7
# Q<10^5
# N<10^9, K<N<10^9 
# n! / ((n-r) ! * r !)

N = int(1e6 + 10)
fact = [1] * N

for i in range(1,N):
    fact[i] = (fact[i-1] * i) % M
    
    
    
q = int(input())
while q:
    factorial =1
    q-=1
    n,r = map(int,input().split())
    factorial = fact[n]
    den = (fact[n-r] * fact[r]) % M
    factorial = (factorial * binary_exponenet(den, M-2, M))%M # only valid for prime number for M.
    print(factorial)
    






