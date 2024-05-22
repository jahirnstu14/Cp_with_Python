
# https://leetcode.com/problems/powx-n/submissions/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n = abs(n)
        if n%2==0:
            return self.myPow(x*x,n//2)
        else:
            return x* self.myPow(x,n-1)
sol = Solution()
x = float(input())
n = int(input())
result = sol.myPow(x,n) 
print(result)