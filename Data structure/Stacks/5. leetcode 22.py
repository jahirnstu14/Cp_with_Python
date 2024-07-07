from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l < r or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            else:
                s.append((x + "(", l + 1, r))
                s.append((x + ")", l, r + 1))
        return res

# Test the function
if __name__ == "__main__":
    sol = Solution()
    test_cases = [3, 4, 1]
    for n in test_cases:
        print(f"n = {n}: {sol.generateParenthesis(n)}")
