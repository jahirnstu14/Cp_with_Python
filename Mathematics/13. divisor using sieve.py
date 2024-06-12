M = int(1e5 + 10)
divisor = [[] for _ in range(M)]

for i in range(1, M):
    for j in range(i, M, i):
        divisor[j].append(i)
        
#  to find divisor every number from 1 to 10        
# for i in range(1,10):
#     print(divisor[i])

num =int(input())
print(len(divisor[num]))
