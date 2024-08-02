# for subsequence it can be order with contiguous and not contiguous

# Why might we want to solve the longest common subsequence problem?

# File comparison. The Unix program "diff" is used to compare two different versions of the same file, to determine what changes have been made to the file. It works by finding a longest common subsequence of the lines of the two files; any line in the subsequence has not been changed, so what it displays is the remaining set of lines that have changed. In this instance of the problem we should think of each line of a file as being a single complicated character in a string.


# nice explanation of solution : https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.

# 1. Bottom up dynamic programming/ tabulization 

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Create a DP table of size (n+1) x (m+1) initialized with -1
    dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]

    # Initialize the base cases:
    # - The length of LCS with an empty string is 0, so dp[i][0] = 0 for all i
    # - The length of LCS with an empty string is 0, so dp[0][j] = 0 for all j
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0

    # Fill in the DP table by considering characters from both strings
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                # If the characters match, increment the LCS length
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                # If the characters do not match, take the maximum of
                # LCS length without one character from s1 or s2
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
    
    # The value in dp[n][m] represents the length of the Longest Common Subsequence
    return dp[n][m]

def main():
    s1 = "acd"
    s2 = "ced"
    print("The Length of Longest Common Subsequence is", lcs(s1, s2))

if __name__ == "__main__":
    main()

# 2. Space Optimization Approach


def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    # Initialize two arrays, 'prev' and 'cur', to store the DP values
    prev = [0] * (m + 1)
    cur = [0] * (m + 1)

    # Loop through the characters of both strings to compute LCS
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                # If the characters match, increment LCS length by 1
                cur[ind2] = 1 + prev[ind2 - 1]
            else:
                # If the characters do not match, take the maximum of LCS
                # by excluding one character from s1 or s2
                cur[ind2] = max(prev[ind2], cur[ind2 - 1])
        
        # Update 'prev' to be the same as 'cur' for the next iteration
        prev = cur[:]

    # The value in 'prev[m]' represents the length of the Longest Common Subsequence
    return prev[m]

def main():
    s1 = "acd"
    s2 = "ced"

    print("The Length of Longest Common Subsequence is", lcs(s1, s2))

if __name__ == '__main__':
    main()

# 3. recursion 

#  class Solution:
#         def longestCommonSubsequence(self, s1: str, s2: str) -> int:
#             return self.helper(s1, s2, 0, 0)
            
#         def helper(self, s1, s2, i, j):
#             if i == len(s1) or j == len(s2):
#                 return 0
#             if s1[i] == s2[j]:
#                 return 1 + self.helper(s1, s2, i + 1, j + 1)
#             else:
#                 return max(self.helper(s1, s2, i+1, j), self.helper(s1, s2, i, j + 1))
            
# 4. recursion with meomziation :


