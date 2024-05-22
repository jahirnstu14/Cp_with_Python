# https://leetcode.com/problems/missing-number/

# solution without bit operation 

nums = list(map(int, input().split()))
# numberlen = len(nums)
# missingnumber = (numberlen*(numberlen+1))//2 - sum(nums)
# print(missingnumber)r


# using exor or bit operation 
result = 0

for i in range(len(nums)+1):
    result^=i
for i in nums:
    result^=i

print(result)


# # solution details :
# # Simple break down of above XOR solution

# numsList = [3,0,1] # Missing number is 2

# result = 0 

# #XOR result with complete number sequence
# for number in range(len(numsList) + 1 ) : # 0, 1, 2 ,3
# 		result ^= number
		
# # Essentially now result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3)

# #XOR result with values in nums
# for num in numsList : # 3,0,1
# 		result ^= num
		
# # result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3) ^ ( 3 ^ 0 ^ 1)

# # XOR of same values cancel each other out 

# # result = (0) ^ (0 ^ 0)  ^ (1^1) ^ (2) ^ (3^3)
# # result =  0 ^ 0 ^ 0 ^ 2 ^ 0
# # result = 2

# return result # 2
    
# another solution using enumerate:

result = 0

for counter,value in enumerate(nums):
    result^=counter+1
    result^=value
print(f"using enumerate we find : {result}");



