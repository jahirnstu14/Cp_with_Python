# Given 2d array a of N*N integers. Given Q queries and in each query given a,b,c and d pring sum of squre represented by (a,b) as top left point and (c,d) as top bottom right point

# Constrainsts
# 1<= N <= 10^3
# 1<=A[I][J]<=10^9
# 1<=Q<=10^5
# 1<=A,B,C,D<=N

# n = int(input())

# # 2d arrary with Create an (n+1) x (n+1) 2D array with 0

# a = [[0]*(n+1) for _ in range(n+1)]

# b = [[0]*(n+1) for _ in range(n+1)] 

# # Create an (n+1) x (n+1) 2D array with empty sublists
# # a = [[] for _ in range(n + 1)]

# # Create a (rows+1) x (cols+1) matrix initialized to 0 if row and colum is different 
# # matrix = [[0] * (cols + 1) for _ in range(rows + 1)]




# # Input the matrix values without using the 0th index
# for i in range(1, n + 1):
#     values = list(map(int, input().split()))
#     for j in range(1, n + 1):
#         a[i][j] = values[j - 1] #without 0 index taking
    
# q = int(input())
# while q:
#     q-= 1
#     ain,b,c,d = map(int,input().split())
#     sum = 0
    
#     for i in range(ain,c+1):
#         for j in range(b,d+1):
#             sum+=a[i][j]
    
#     print(sum)
    
    
# time complexity for above program is 0(N^2) + 0(Q*N^2) = 10^5 * 10^6 = 10^11



n = int(input())

# 2d arrary with Create an (n+1) x (n+1) 2D array with 0

a = [[0]*(n+1) for _ in range(n+1)]

p = [[0]*(n+1) for _ in range(n+1)] 

# Input the matrix values without using the 0th index
for i in range(1, n + 1):
    values = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = values[j - 1] #without 0 index taking
        p[i][j] = a[i][j] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]
        

    
q = int(input())
while q:
    q-= 1
    ain,b,c,d = map(int,input().split())
    sum = 0
    
    sum = p[c][d] - p[ain-1][d] - p[c][b-1] + p[ain-1][b-1]
    
    print(sum)
    
    
    

    
