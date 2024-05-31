# https://leetcode.com/problems/contains-duplicate/

# most effiecient solution using hashmap and dictionary

nums = list(map(int,input().split()))
d ={}
flag = 0
for i in nums:
    d[i]=0
for i in nums:
    d[i]+=1
    
for key,values in d.items():
    if d[key]>=2:
        flag =1
        break
if flag:
    print("True")
else:
    print("False")



# below it is correct but leetcode donot accept :

# List = list(map(int,input().split()))
# max = 10**5

# hash=[0]* max
# module = 1e7+10


# for value in List:
#     hash[int(value%module)]+=1
    
# flag = 0
    
# for i in List:
#     if hash[i]>=2:
#         flag = 1
#         break
    
    
# if flag:
#     print("True")
# else:
#     print("False")


#  time complexity o(n*logn)

# flag = 0

# # nums = list(map(int,input().split()))

# nums.sort()
# for i in range(len(nums)-1):
#     if nums[i]==nums[i+1]:
#         flag = 1
#         break

# if flag:
#     print("True")
# else:
#     print("False")

# using counter function 
# Explanation: Counter is a subclass of dict designed for counting hashable objects in Python. It’s a dictionary that stores the objects as keys and the frequencies of those objects as values. In this approach, we utilize Counter to count the frequencies of each integer for us. For example, if the input array is [1, 2, 3, 4, 4, 5], using Counter on that input array will give us the following dictionary: Counter({4: 2, 1: 1, 2: 1, 3: 1, 5: 1}). Utilizing this function, we will loop through the freq dictionary to see if any values (frequencies) are greater than 1, which means there exists an integer in the given array that is duplicated.

# nums = list(map(int,input().split()))
# freq = Counter.nums

# for num,freq in freq.items():
#     if freq>=1:
#         return True
#     return False 
    
# last code copy of first code :
nums = list(map(int,input().split()))
d ={}
flag = 0
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for key,values in d.items():
    if d[key]>=2:
        flag =1
        break
if flag:
    print("True")
else:
    print("False")