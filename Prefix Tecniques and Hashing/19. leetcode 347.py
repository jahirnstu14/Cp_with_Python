# Using enumerate on Dictionary Keys
# When you use enumerate on a dictionary's keys, you get an index along with each key. This can be useful if you need to know the position of each key in the dictionary's order.

# Example:
# python
# Copy code
# frequency = {1: 5, 2: 3, 3: 9, 4: 7}

# # Using enumerate on dictionary keys
# for index, key in enumerate(frequency.keys()):
#     print(f"Index: {index}, Key: {key}, Value: {frequency[key]}")

# yaml
# Copy code
# Index: 0, Key: 1, Value: 5
# Index: 1, Key: 2, Value: 3
# Index: 2, Key: 3, Value: 9
# Index: 3, Key: 4, Value: 7

# Using items() Method
# When you use the items() method, you get both the key and the corresponding value directly in each iteration. This is more straightforward if you need to work with both keys and values.

# Example:
# python
# Copy code
# frequency = {1: 5, 2: 3, 3: 9, 4: 7}

# # Using items() method
# for key, value in frequency.items():
#     print(f"Key: {key}, Value: {value}")
# Output:
# mathematica
# Copy code
# Key: 1, Value: 5
# Key: 2, Value: 3
# Key: 3, Value: 9
# Key: 4, Value: 7


# problem solving Start

from collections import defaultdict

nums = list(map(int,input().split()))
k = int(input())


hashmap = defaultdict(int)

for num in nums:
    hashmap[num]+=1
    
# when used empty dictionary:
# for num in nums:
#     if num not in frequency:
#         frequency[num] = 1
#     else:
#         frequency[num] = frequency[num] + 1

frequency =  dict(sorted(hashmap.items(),key = lambda x:x[1],reverse=True))

result = []

for index,key in enumerate(frequency.keys()):
    if index>=k:
        break
    result.append(key)
    
    
    
print(result)
    



