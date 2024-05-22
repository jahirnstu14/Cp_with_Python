# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/friends-relationship-1/

n = int(input())

for i in range(n):
    k=int(input())
    for i in range(k):
        for j in range(2*k):
            if j>=i+1 and j<2*k-(i+1):
                print("#",end=" ")
            else:
                print("*",end=" ")
        print()

