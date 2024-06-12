# https://codeforces.com/problemset/problem/230/B

M = int(1e5 + 10)
divisor = [[] for _ in range(M)]

for i in range(1, M):
    for j in range(i, M, i):
        divisor[j].append(i)
        
#  to find divisor every number from 1 to 10        
# for i in range(1,10):
#     print(divisor[i])

n =int(input())
array = list(map(int,input().split()))

for i in array:
    if (len(divisor[i]))==3:
        print("YES")
    else:
        print("NO")
