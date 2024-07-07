# nice discussion : https://leetcode.com/problems/pass-the-pillow/discuss/5425272/Beats-100.00-of-users-with-Javaoror-Simple-and-Easy-Well-Explained-Math-Solution


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        completed = time // (n - 1)
        remaining = time % (n - 1)
        ans = 0
        if completed % 2 != 0:
            ans = n - remaining
        else:
            ans = remaining + 1
        return ans

# Example usage:
solution = Solution()
print(solution.passThePillow(5, 10))  # Example call to the method
