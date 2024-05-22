# https://www.codechef.com/problems/FLOW006

n = int(input())

for i in range(n):
    k = int(input())
    
    sum=0
    while k>0:
        remainder = k%10
        sum+=remainder
        k//=10
    print(f"{sum}")
    
