# https://www.hackerrank.com/challenges/30-arrays/problem


k = int(input())

n = list(map(int,input().split()))

for i in reversed(n):
    print(i,end=" ")

