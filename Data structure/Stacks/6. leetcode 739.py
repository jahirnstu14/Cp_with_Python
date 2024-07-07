# super solution with great explanation : https://leetcode.com/problems/daily-temperatures/
# another way solution in multiple way : https://leetcode.com/problems/daily-temperatures/discuss/1574808/C%2B%2BPython-3-Simple-Solutions-w-Explanation-Examples-and-Images-or-2-Monotonic-Stack-Approaches

# ❌ Solution - I (Brute-Force)

# Let's see how we can solve this using brute-force approach.

# For each index i, we can just iterate over the array till we either find the the 1st index j such that T[j] > T[i] or reach the end of array.
# If we find j such that T[j] > T[i], we have ans[i] = j-i.
# Otherwise, ans[i] = 0

# class Solution:
#     def dailyTemperatures(self, T):
#         ans = [0]*len(T)
#         for i in range(len(T)):
#             for j in range(i+1, len(T)):
#                 if T[j] > T[i]:
#                     ans[i] = j-i
#                     break
#         return ans # time complexity 0(n^2) and space complexity 0(n)
    
# ✔️ Solution - II (Decreasing Monotonic Stack)
from collections import deque
# forward way and start from front
class Solution:
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        s = deque()
        
        for cur , cur_temp in enumerate(T):
            while s and cur_temp > T[s[-1]]:
                prev = s.pop()
                ans[prev] = cur - prev
            s.append(cur)
            
        return ans
# for deque characteristics it gives s[-1]  and s.pop() will give index otherwise , they will give value 
      
s1 = Solution()  
print(s1.dailyTemperatures([73,74,75,71,69,72,76,73]))

    
  
# ✔️ Solution - III (Monotonic Stack - 2)
# from backward way and start from last
# class Solution:
#     def dailyTemperatures(self, T):
#         ans, s = [0]*len(T), deque()
#         for cur in range(len(T)-1,-1,-1):
#             while s and T[s[-1]] <= T[cur]:
#                 s.pop()
#             ans[cur] = s[-1] - cur if s else 0
#             s.append(cur)
#         return ans