# problem link : https://codeforces.com/problemset/problem/266/B
    
n, t = map(int, input().split())

d = list(input())

for i in range(t):
    j = 0
    while j < n-1:
        if d[j] == 'B' and d[j+1] == 'G':
            d[j], d[j+1] = d[j+1], d[j]
            j+=1
        j+=1
print("".join(d))
