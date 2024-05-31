# nice solution link like interviewwer asked link: https://leetcode.com/problems/product-of-array-except-self/discuss/1342916/3-Minute-Read-Mimicking-an-Interview

# n = int(input())
# a= list(map(int,input().split()))

# prefix = [0] * n
# postfix = [0] * n

# prefix[0]=1
# postfix[n-1]=1

# for i in range(1,n):
#     prefix[i] = prefix[i-1] * a[i-1]
#     print(prefix[i])
    

  
# for i in range(n-2,-1,-1):
#     postfix[i] = postfix[i+1] * a[i+1]
    
# ans = []

# for i in range(n):
#     product =prefix[i] * postfix[i]
#     ans.append(product)
    
# print(ans)

# with time complexity 0(n):

n = int(input())
nums= list(map(int,input().split()))
ans = [1] * n
cur = 1


# forward pass product 

for i in range(n):
    ans[i]*=cur
    cur*=nums[i]

cur = 1

for i in range(n-1,-1,-1):
    ans[i]*=cur
    cur*=nums[i]
    
print(ans)











