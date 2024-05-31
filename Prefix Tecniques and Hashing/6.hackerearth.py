# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/a-needle-in-the-haystack-1/

# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/bob-and-string-easy/

t = int(input())
while t:
    t-=1
    s1 = input().strip()
    s2 = input().strip()
    
    a = [0]*26
    b = [0]*26
    flag=0
    
    len1 = len(s1)
    len2 = len(s2)
    
    for char in s1:
        a[ord(char)-ord('a')]+=1
    for char in s2:
        b[ord(char)-ord('a')]+=1
        
    for i in range(26):
        if a[i]<=b[i]:
            flag = 1
            break
        
    if flag:
        print("NO")
    else:
        print("YES")
            
    
    
    