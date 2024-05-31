# https://www.hackerrank.com/challenges/crush/problem

# brute force method
# n,m = map(int,input().split())
# arr = [0] * (n+1)

# while m:
#     m-=1
#     a,b,d = map(int,input().split())
    
#     for i in range(a,b+1):
#         arr[i]+=d
    
#     mx = -1
    
#     # manual method
#     # for i in range(1,n+1):
#     #     if mx<=arr[i]:
#     #         mx = arr[i]
    
#     mx = max(arr) # max function complexit is 0(N) for N size list 
            
# print(mx)
    
# time complexity : 0(M*N+N)= 2*10^5 * 10^7 = 10^12 , so, it is not possible for 1s second execution. 
 
# for reducing complexity , we use hasing + prefix sum 

n,m = map(int,input().split())
arr = [0] * (n+2)

while m:
    m-=1
    a,b,d = map(int,input().split())
    
    arr[a]+=d
    arr[b+1]-=d
    
for i in range(1,n+1):
    arr[i] += arr[i-1]

mx = -1

# manual method
# for i in range(1,n+1):
#     if mx<=arr[i]:
#         mx = arr[i]

mx = max(arr) # max function complexit is 0(N) for N size list  
            
print(mx)

# time complexity : 0(M+N)= 2*10^5  = 10^12 , so, it is possible for 1s second execution.

