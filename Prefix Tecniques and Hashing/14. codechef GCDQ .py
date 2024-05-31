# Read problems statements in Mandarin Chinese and Russian.
# You are given an array A of integers of size  N. You will be given Q queries where each query is represented by two integers L,R. You have to find the gcd (Greatest Common Divisor) of the array after excluding the part from range L to R inclusive (1 Based indexing). You are guaranteed that after excluding the part of the array remaining array is non empty.

# First line of input contains an integer T denoting number of test cases.
# For each test case, first line will contain two space separated integers N,Q.
# Next line contains N space separated integers denoting array A.
# For next Q lines, each line will contain a query denoted by two space separated integers 

# Output
# For each query, print a single integer representing the answer of that query.

# Constraints
# Subtask #1: 40 points
# 2≤T,N≤100, 1≤Q≤N, 1≤A[i]≤10^5 
# 1≤L,R≤N and L≤R
# Subtask #2: 60 points
# 2≤T,N≤10^5,1≤Q≤N, 1≤A[i]≤10^5,
# 1≤L,R≤N and L≤R
# Sum of N over all the test cases will be less than or equal to 10^6

# INPUT :
# 1
# 3 3
# 2 6 9
# 1 1
# 2 2
# 2 3

# OUPUT:
# 3
# 1
# 2

# brute force method 
# import math

# t = int(input())

# while t:
#     t-=1
#     n, q = map(int, input().split())
#     a = [0] * (n + 1)  # Create an array of size n+1 initialized to 0
#     input_values = list(map(int, input().split()))
    
#     # Fix the loop range, it should be range(1, n + 1)
#     for i in range(1, n + 1):
#         a[i] = input_values[i - 1]  # Corrected indexing
        
#     while q:
#         q-=1
#         l,r = map(int,input().split())
#         gcd = 0
#         for i in range(1,l):
#             gcd = math.gcd(gcd,a[i])
#         for i in range(r+1,n+1):
#             gcd = math.gcd(gcd,a[i])
            
#         print(gcd)
        
# N=100,N=Q time complexity : 0(T*(0(N)+0(Q*N)) = 0(T*Q*N) = 100^3 . if wish t is not same as N . then time complexity 0(2*100^2) so, it is possible .it is occured because of assumption . SO, IT WILL BE PASSED FOR FIRST SUBTASK

# FOR SECOND SUBTASK AND N = 10^5
# time complexity : 0(T*(0(N)+0(Q*N)) = 0(T*Q*N) = 0(N)= (10^5)^3 = 10^15 SO, IT IS NOT POSSIBLE EXECUTED IN 1S SECOND FROM VALUE T,N,Q WE SELECT N VALUE BECAUSE OF WORST OR HIGHEST VALUE OF N . IF IT RUN THEN ALL CASE WILL BE RUN. FOR THIS T IS CONSIDEREED N . AND TIME COMPLEXITY IS GOING TO BE 0(N^3)


import math

t = int(input())

while t:
    t -= 1
    n, q = map(int, input().split())
    a = [0] * (n + 1)  # Create an array of size n+1 initialized to 0
    forward = [0] * (n + 2)  # Initialize forward with size n+2
    backward = [0] * (n + 2)  # Initialize backward with size n+2
    
    input_values = list(map(int, input().split()))
    
    # Fix the loop range, it should be range(1, n + 1)
    for i in range(1, n + 1):
        a[i] = input_values[i - 1]  # Corrected indexing
         
    for i in range(1, n + 1):
        forward[i] = math.gcd(forward[i - 1], a[i])  # the complexity for gcd is log max(a,b)
    for i in range(n, 0, -1):
        backward[i] = math.gcd(backward[i + 1], a[i])
        
    while q:
        q -= 1
        l, r = map(int, input().split())
        gcd = math.gcd(forward[l - 1], backward[r + 1])
            
        print(gcd)

        
# time complexity : 0(T*(N+Q)) = 0(T*(N+N)) = 10^6 


        
            