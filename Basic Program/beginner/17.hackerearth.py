# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/


k = int(input())

for i in range(k):

    n,r = map(int,input().split())
    m = list(map(int,input().split()))
    m.sort()
    
    if m[0]<=r:
        print(r-m[0])
    else:
        print(0)
        


