# https://www.hackerearth.com/problem/algorithm/monk-and-divisor-conundrum-56e0eb99/
import math
from collections import defaultdict
N = int(2e5 + 10)
hash = [0] * N
multiple_count = [0] *  N

n = int(input())
for _ in range(n):
    x = int(input())
    hash[x]+=1
    
    
for i in range(1,N):
    for j in range(i,N,i):
        multiple_count[i]+=hash[j]
        

    
query = int(input())
while query:
    query-=1
    p,q = map(int,input().split())
    lcm  = (p*q)//(math.gcd(p,q))
    ans = multiple_count[p] + multiple_count[q]
    ans-=multiple_count[lcm]  
    print(ans)  
    