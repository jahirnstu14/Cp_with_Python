# https://leetcode.com/problems/single-number/

n = int(input())
ans=0

for i in range(n):
    k = int(input().split())
    ans^=k

print(ans)

# below solution description

# for this wehn do exor then it will vanish same nubmer by replacing . 
# According to this gate , the output is true , only if both the inputs are of opposite kind .
# That is ,
# A B Y
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

# We apply the extended version of this gate in our bitwise XOR operator.
# If we do "a^b" , it means that we are applying the XOR gate on the 2 numbers in a bitwise fashion ( on each of the corresponding bits of the numbers).
# Similarly , if we observe ,

# A^A=0
# A^B^A=B
# (A^A^B) = (B^A^A) = (A^B^A) = B This shows that position doesn't matter.
# Similarly , if we see , a^a^a......... (even times)=0 and a^a^a........(odd times)=a