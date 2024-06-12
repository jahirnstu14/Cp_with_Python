# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/?currentPage=1&orderBy=most_votes&query=


    # Time Complexity : O(N^2), Where N is the size of the Array(prices). As we check for possible pair, and the
    # total number of pairs are : N*(N–1)/2.

    # Space complexity : O(1), Constant space.
    
# brute force method

# prices = list(map(int,input().split()))

# n = len(prices)
# max_profit = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if prices[j] - prices[i] > max_profit:
#             max_profit = prices[j] - prices[i]
# print(max_profit)

# using slding windows 

prices = list(map(int,input().split()))

n = len(prices)

left = 0
right = 1
maxprofit = 0

while right < n:
    maxprofit  = max(maxprofit,prices[right]-prices[left])
    
    if prices[left]>prices[right]:
        left = right
        right+=1
    else:
        right+=1
print(maxprofit)





#  another solve using another array creating and incresing space complexity       

#  Time Complexity : O(N), As we iterate the array(prices) two times. Where N = size of the array.

#     Space complexity : O(N), Array(maxPrices) space.

#     Solved using Dynamic Programming Approach(tabulation).

# n = len(prices)
# if n == 0:
#     print(0)

# maxPrices = [0] * n
# maxPrices[n-1] = prices[n-1]

# for i in range(n-2, -1, -1):
#     maxPrices[i] = max(maxPrices[i+1], prices[i])

# maxProfit = 0
# for i in range(n):
#     maxProfit = max(maxProfit, maxPrices[i] - prices[i])

# print(maxProfit);
        

