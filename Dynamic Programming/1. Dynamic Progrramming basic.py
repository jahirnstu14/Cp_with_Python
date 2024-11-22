# for interview preparation : last e dekbo
# Dynamic Programming : ***
# Basic Recursion and Dynamic Programming ***
# 0–1 Knapsack **
# Coin Change **
# Longest Increasing Subsequence **
# Longest Common Subsequence **




# dynamic programmming is used for recursive problem optimal solution .
# nicely describe dp link : https://www.youtube.com/watch?v=5dRGRueKU3M&list=PLJULIlvhz0rE83NKhnq7acXYIeA0o1dXb

# also another blog for dp : https://takeuforward.org/data-structure/dynamic-programming-introduction/

# The two common dynamic programming approaches are:

# Memoization: Known as the “top-down” dynamic programming, usually the problem is solved in the direction of the main problem to the base cases.
# Tabulation: Known as the “bottom-up '' dynamic programming, usually the problem is solved in the direction of solving the base cases to the main problem.

# recursion problem for fibbonacci number:
# f(n){
#     if n<=1:
#         return n 
#     return f(n-1) + f(n-2)
# }

# example of memoization :

def f(n, dp):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    dp[n] = f(n-1, dp) + f(n-2, dp)
    return dp[n]

if __name__ == "__main__":
    n = 5
    dp = [-1] * (n+1)
    print(f(n, dp))
    

# Time Complexity: O(N)

# Reason: The overlapping subproblems will return the answer in constant time O(1). Therefore the total number of new subproblems we solve is ‘n’. Hence total time complexity is O(N).

# Space Complexity: O(N)

# Reason: We are using a recursion stack space(O(N)) and an array (again O(N)). Therefore total space complexity will be O(N) + O(N) ≈ O(N)


# tabulation method : Tabulation is a ‘bottom-up’ approach where we start from the base case and reach the final answer that we want.

from typing import List

def main():
    n = 5
    dp = [-1]*(n+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n])

if __name__ == "__main__":
    main()
    
# Time Complexity: O(N)
# Reason: We are running a simple iterative loop
# Space Complexity: O(N)
# Reason: We are using an external array of size ‘n+1’.

# space optimization : 

def main():
    n = 5

    prev2 = 0
    prev = 1

    for i in range(2, n+1):
        cur_i = prev2 + prev
        prev2 = prev
        prev = cur_i
    print(prev)

if __name__ == "__main__":
    main()
    
# Time Complexity: O(N)
# Reason: We are running a simple iterative loop
# Space Complexity: O(1)
# Reason: We are not using any extra space