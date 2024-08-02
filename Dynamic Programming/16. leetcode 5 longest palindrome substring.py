# Nicely describe : https://leetcode.com/problems/longest-palindromic-substring/discuss/4212564/Beats-96.49-oror-5-Different-Approaches-oror-Brute-Force-oror-EAC-oror-DP-oror-MA-oror-Recursion-oror


# brute force solution : 

# Intuition :
# The obvious brute force solution is to pick all possible starting and ending positions for a substring, and verify if it is a palindrome. There are a total of n^2 such substrings (excluding the trivial solution where a character itself is a palindrome). Since verifying each substring takes O(n) time, the run time complexity is O(n^3).

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len = 1
        Max_Str = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > Max_Len and s[i:j + 1] == s[i:j + 1][::-1]:
                    Max_Len = j - i + 1
                    Max_Str = s[i:j + 1]

        return Max_Str

# Function to take input and test the solution
def main():
    s = input("Enter the string: ")
    solution = Solution()
    result = solution.longestPalindrome(s)
    print("The longest palindromic substring is:", result)

# Run the main function to test the solution
if __name__ == "__main__":
    main()

# Time complexity : ***O(n^3)***. Assume that n is the length of the input string, there are a total of C(n, 2) = n(n-1)/2 substrings 
# Space complexity : ***O(1)***.

# Approach 2: Expand Around Center
# Intuition :
# To enumerate all palindromic substrings of a given string, we first expand a given string at each possible starting position of a palindrome and also at each possible ending position of a palindrome and keep track of the length of the longest palindrome we found so far.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
    
    
# Time complexity : ***O(n^2)***. Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
# Space complexity : ***O(1)***.

# Approach 3: Dynamic Programming
# Intuition : To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str

# Time complexity : ***O(n^2)***. This gives us a runtime complexity of O(n^2).
# Space complexity : ***O(n^2)***. It uses O(n^2) space to store the table.

# Approach 4: Manacher's Algorithm

# intuition : To avoid the unnecessary validation of palindromes, we can use Manacher's algorithm. The algorithm is explained brilliantly in this article. The idea is to use palindrome property to avoid unnecessary validations. We maintain a center and right boundary of a palindrome. We use previously calculated values to determine if we can expand around the center or not. If we can expand, we expand and update the center and right boundary. Otherwise, we move to the next character and repeat the process. We also maintain a variable max_len to keep track of the maximum length of the palindrome. We also maintain a variable max_str to keep track of the maximum substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return Max_Str
    
# Time complexity : ***O(n)***. Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n).
# Space complexity : ***O(n)***. It uses O(n) space to store the table.

