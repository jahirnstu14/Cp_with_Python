# Ordinally method

# question :  Given T test cases and in each test case
# a number N. Print its factorial for each test case % M 
# where M =  10^9 + 7

# constraints:
#     1<=T<=10^5
#     1<=N<=10^5 

# t = int(input())
# M = 1e7+10

# while t:
#     fact = 1
#     n = int(input())
    
#     for i in range(2,n+1):
#         fact = (fact * i) % M
#         fact = int(fact)
#     t = t-1
        
#     print(fact) # time complexit will be o(T)+o(n)= 10^5 + 10^5 =10^10
    


# after using prefix tecnique
t = int(input())
M = int(1e7+10)

N = int(input())
fact = [1,1]

for i in range(2,N+1):
    fact.append((fact[i-1]*i)%M)

for _ in  range(t):
    print(fact[N]) # complexity is O(T)+O(N) =10**5


