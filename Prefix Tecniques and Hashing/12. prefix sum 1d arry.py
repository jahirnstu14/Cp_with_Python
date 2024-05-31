# Given array a of N intergers. Given Q queries and in each query given L and R print sum of array elements from index L to R (L,R INCLUDED)

# CONSTRAINSTS
# 1<=N<=10^5
# 1<=A[I]<=10^9
# 1<=Q<=10^5
# 1<=L,R<=N


# n = int(input())
# array = list(map(int,input().split()))
# q = int(input())


# while q:
#     q-=1
#     sum = 0
#     L,R = map(int,input().split())
#     for i in range(L-1,R):
#         sum+=array[i]
#     print(sum)
    
    
    # and complexity is 0(N) + 0(Q+N) = 10^10 so, it is notp possible run in 1s second.
    
    
n = int(input())
array1 = [0] * (n+1)
array2 = [0] * (n+1)
input_values = list(map(int,input().split()))

for i in range(1,n+1):
    array1[i]=input_values[i-1]


q = int(input())

for i in range(1,n+1):
    array2[i] = array2[i-1] + array1[i] 


while q:
    q-=1
    L,R = map(int,input().split())
    ith_sum = array2[R]-array2[L-1]
    print(f"{ith_sum}")
    


# time complexit will 0(N) = 10^5 , it is possible to execute in 1s second 
    
    