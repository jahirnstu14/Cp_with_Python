# logic behind the above program : https://leetcode.com/problems/koko-eating-bananas/discuss/1705145/Python-BinarySearch-%2B-Optimizations-or-Explained

# brute force tecnique : 
import math
piles = list(map(int,input().split()))
H = int(input())

# n = len(piles)
maximum = max(piles)

# for i in range(1, maximum+1):
#     sum = 0
#     for j in range(n):
#         ithvalue = math.ceil(piles[j] / i) # time complexity will be 0(n^2) and space complexity will be 0(1)
#         sum += ithvalue
#     if sum<=h:
#         print(i)
#         break
    
    
# Now the optimization solution will be :

low, high = 1, max(piles)  # Using the maximum pile size as the upper bound
        
while low <= high:
    k = (low + high) // 2
    h = 0
    for pile in piles:
        h += math.ceil(pile / k)  # Using a simple for loop to calculate hours
    
    if h > H:
        low = k + 1
    else:
        high = k - 1
        
print(low) 
    
    
    
    

