# solution description llink : https://leetcode.com/problems/multiply-strings/discuss/1563536/C%2B%2B-Simple-Solution-w-Explanation-and-Images-or-School-%2B-Optimized-Multiplication

# most optimal solution with complexity : time complexity(m*n) and space complexity 0(1)

A  = input() # 123 
B = input() #456

if A=='0'or B=='0':
    print(0)

ans = ['0'] * (len(A)+len(B))

for i in range(len(A)-1,-1,-1):
    for j in range(len(B)-1,-1,-1):
        res = int(ans[i+j+1]) + int(A[i]) * int(B[j])
        ans[i+j+1] = str(res%10)
        ans[i+j] = str(int(ans[i+j]) + int(res//10))
        
ans =''.join(ans)
if ans[0]=='0':
    print(ans[1:])
print(ans)


