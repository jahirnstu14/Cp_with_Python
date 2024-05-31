# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/little-jhool-and-the-magical-jewels/

t = int(input())
while t:
    t-=1
    s1 = input().strip()
    
    
    a = [0]*26
   
    count = 0
    
    len1 = len(s1)
    
    
    for char in s1:
        a[ord(char)-ord('a')]+=1
    
        
    minimum = min(a[ord('r')-ord('a')],a[ord('u')-ord('a')],a[ord('b')-ord('a')],a[ord('y')-ord('a')],)
    
    print(minimum)