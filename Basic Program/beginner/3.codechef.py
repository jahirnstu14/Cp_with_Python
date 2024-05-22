# https://www.codechef.com/LRNDSA01/problems/FLOW007


n = int(input())

for i in range(n):
    k = int(input())
    
    i=0
    remainder=0
    while k>0:
        remainder=remainder*10 + k%10
        k//=10
        i+=1
    print(f"{remainder}")
    
