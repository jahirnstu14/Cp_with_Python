# https://leetcode.com/problems/number-of-1-bits/

n = int(input())

count=0
while(n):
    if(n&1):#extract the last bit from binary 
        count+=1
    n=n>>1
print(count)





# anther solution will be 
n=11

count=0
while n:
    n=n&(n-1)
    count+=1
    
print(count)