
s = input().strip()
t = input().strip()

a = [0]*26
b = [0]*26
flag=0

len1 = len(s)
len2 = len(t)

for char in s:
    a[ord(char)-ord('a')]+=1
for char in t:
    b[ord(char)-ord('a')]+=1
    
for i in range(26):
    if a[i]!=b[i]:
        flag = 1
        break
    
if flag:
    print("false")
else:
    print("true")