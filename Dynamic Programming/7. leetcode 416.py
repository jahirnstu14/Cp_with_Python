# nice explanation : https://takeuforward.org/data-structure/partition-equal-subset-sum-dp-15/
# another nice explanation : https://leetcode.com/problems/partition-equal-subset-sum/discuss/462699/Whiteboard-Editorial.-All-Approaches-explained.

def canPartition(n, arr):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)
    
    # If the total sum is odd, it cannot be partitioned into two equal subsets.
    if totSum % 2 == 1:
        return False
    else:
        # Calculate the target sum for each subset.
        k = totSum // 2
        
        # Initialize a dynamic programming table (dp) to store subproblem results.
        dp = [[False for j in range(k + 1)] for i in range(n)]

        # Initialize the base case: An empty subset can always achieve a sum of 0.
        for i in range(n):
            dp[i][0] = True

        # Initialize the base case for the first element in the array.
        if arr[0] <= k:
            dp[0][arr[0]] = True

        # Fill in the DP table using a bottom-up approach.
        for ind in range(1, n):
            for target in range(1, k + 1):
                # If the current element is not taken, the result is the same as the previous row.
                notTaken = dp[ind - 1][target]
                
                # If the current element is taken, subtract its value from the target and check the previous row.
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]
                
                # Update the DP table with the result of taking or not taking the current element.
                dp[ind][target] = notTaken or taken
        
        # The final result is stored in the bottom-right cell of the DP table.
        return dp[n - 1][k]

def main():
    arr = [2, 3, 3, 3, 4, 5]
    n = len(arr)
    
    # Check if the array can be partitioned into two equal subsets and print the result.
    if canPartition(n, arr):
        print("The Array can be partitioned into two equal subsets")
    else:
        print("The Array cannot be partitioned into two equal subsets")

if __name__ == '__main__':
    main()
    
    
# another way to solve this problem

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total_sum = sum(nums)
        
#         if total_sum % 2 == 1:
#             return False
#         target = total_sum // 2
        
#         n = len(nums)
#         dp = [False] * (target + 1)
#         dp[0] = True
        
#         for num in nums:
#             for i in range(target, num - 1, -1):
#                 dp[i] = dp[i] or dp[i - num]
        
#         return dp[target]
    
# def main():
#     arr = [2, 3, 3, 3, 4, 5]
#     n = len(arr)
    
#     # Check if the array can be partitioned into two equal subsets and print the result.
#     if canPartition(n, arr):
#         print("The Array can be partitioned into two equal subsets")
#     else:
#         print("The Array cannot be partitioned into two equal subsets")

# if __name__ == '__main__':
#     main()


