# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

s1 = input()
s2=s1[::-1]

if s1==s2:
    print("YES")
else:
    print("NO")