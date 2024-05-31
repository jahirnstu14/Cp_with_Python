# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/xsquare-and-double-strings-1/?filter=all&sort=most-likes

# one solution 

t = int(input())
while t:
    t=t-1
    s = input().strip()
    a = [0]*26
    flag = 0
    
    for char in s:
        a[ord(char)-ord('a')]+=1
        if  a[ord(char)-ord('a')]>=2:
            flag =1
            break
    
    if flag:
        print("Yes")
    else:
        print("No")
        
        
        
# another solution :

for _ in range(int(input())):
    s = input().strip()
    x = list(s)
    
    d ={}
    
    for i in s:
        d[i]=0
        
    for i in s:
        d[i]=d[i]+1
        
    for i in d: # only takes the key values  
        if d[i]==1:
            x.remove()
            
    if len(x)!=0:
        print('Yes')
    else:
        print("No")
    