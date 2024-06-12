# https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/name-count/

M = int(1e9+10)
N= int(1e5+10)
fact=[1] * (N+1)

def binary_exponenet(a,b,m):
    result = 1
    while b>0:
        if b&1:
            result = (result * b) % M      # the complexity of this function is logb(b number of bits in binary of power )
        a = (a * a)% M
        b>>=1
    return result


# Alphabet -->K symbols , N size passwrod , k>None
# KCN---> N! * KCN
# a,b,c -->> 3* 2 * 1 --->n! 

t = int(input())
fact[0] = 1
for i in range(N):
    fact[i] = (fact[i-1] * i) % M

while t:
    t-=1
    n,k = map(int,input().split())
    ans = fact[n]
    ans = (ans * fact[k]) % M
    den = (fact[k-n] * fact[n]) % M
    ans = (ans * binary_exponenet(den,M-2,M))% M
    print(ans)

