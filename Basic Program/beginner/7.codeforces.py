# https://codeforces.com/contest/1102/problem/A

n = int(input())
n%=4
if n==0 or n==3:
    print(0)
else:
    print(1)