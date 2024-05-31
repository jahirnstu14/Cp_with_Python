# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/pair-sums/?fbclid=IwAR2XcdRMJnGwG3ojY4diVU80L41VtxP85xk2VWMZ_lUYz58kKYk2TtZN3rc

n,k = map(int,input().split())

list1= list(map(int,input().split()))

list1.sort()
i=0
j=n-1
sum = 0
flag =0

while i<j:
    sum = list1[i]+list1[j]
    if sum==k:
        flag = 1
        break
    
    elif sum>k:
        j-=1
    else:
        i+=1
        
        
if flag:
    print("Yes")
else:
    print("No")
        
    