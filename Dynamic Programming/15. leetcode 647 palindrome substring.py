# nicely describe solution : https://leetcode.com/problems/palindromic-substrings/discuss/4703811/Interview-Approach-or-3-Approach-(-Brute-Force-Expand-Middle-DP-)


# for subsequence -----> not contiguous , sequence
# for substring  ------> contiguous, sequence
# for subset     ------> not contiguous, not sequence : it is important to know this topic . 

# brute force method 


class Solution:
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:  
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    ans += 1
        return ans

# Example usage
if __name__ == "__main__":
    s = "abc"  # Default input
    solution = Solution()
    print(solution.countSubstrings(s))

# optimize solution 

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            even = self.palindromeCount(s, i, i + 1)
            odd = self.palindromeCount(s, i - 1, i + 1)
            ans += even + odd + 1
        return ans

    def palindromeCount(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

# Example usage
solution = Solution()
print(solution.countSubstrings("abc"))  # Output: 3
print(solution.countSubstrings("aaa"))  # Output: 6

# dynamic programming 

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        ans = 0

        # Single character substrings
        for i in range(n):
            palindrome[i][i] = True
            ans += 1

        # Two character substrings
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrome[i][i + 1] = True
                ans += 1

        # Substrings of length 3 and greater
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                if s[i] == s[i + length - 1] and palindrome[i + 1][i + length - 2]:
                    palindrome[i][i + length - 1] = True
                    ans += 1

        return ans

# Example usage
solution = Solution()
s = input("Enter a string: ")
print(solution.countSubstrings(s))


