#https://leetcode.com/problems/reverse-bits/discuss/54748/AC-Python-44-ms-solution-bit-manipulation

n = int(input())

ans = 0

for i in range(32):
    ans = (ans<<1)|n&1
    n>>=1
print(ans)
    
    