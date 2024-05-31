#  given array a of N integers. Given Q queries and in each query given a number x, print count of that number in a array 
# constraints:
#     1<=N<10^5
#     1<=a[i]<=10^7
#     1<=Q<=10^5


# without reducing complexity 

# N =  int(input(" Enter the number of arry : "))
# list1 = list(map(int,input().split()))

# q = int(input(" ENTER THE number of QUERY : "))

# while q :
#     check = int(input())
#     ct = 0
#     for i in range(len(list1)): #time complexity : 0(N) + 0(q*N) = 0(10^5 * 10^5 =10^10) =10^10 it is not possible in 1s second 
#         if(list1[i]==check):
#             ct = ct+1
#     print(ct)
#     q = q-1
    
    
    
# using prefix method

n = int(input("Enter the number of array : "))
a=[]

hash = [0]*(n+1)
print("Taking the input array : ")

for i in range(n):
    value = int(input())
    a.append(value)
    hash[value]+=1
    
    
q = int(input("Enter the number of query : "))  #// for this complexity will be : 0(N)= 10^5 SO, IT IS POSSIBLE TO RUN IN 1S 
while q:
    check = int(input())
    print(hash[check])
    q=q-1
    
    
    
    
    


        