# https://www.youtube.com/watch?v=zwlCeWUGlE0

t = int(input())
while t:
    t-=1
    n,q = map(int,input().split())
    s = input()
    while q:
        q-=1
        l,r = map(int,input().split())
        hash = [0] * 26
        
        for i in range(26):
            hash[i]=0
        l-=1
        r-=1 # becasue , indexing of string start from 0
        
        for i in range(l,r+1):
            hash[ord(s[i])-ord('a')]+=1
            
        oddcount = 0
        
        for i in range(26):
            if(hash[i]%2!=0):
                oddcount+=1
        if oddcount>1:
            print("NO")
        else:
            print("YES")
            
# time complexity : 0(t*(n+q*(26+n+26)))
# 0(t*q*n) = 10 * 10^5 * 10^5



t = int(input())
N = 10**5
hash = [[0 for _ in range(26)] for _ in range(N)]
while t:
    t-=1
    n,q = map(int,input().split())
    s = input()
    for i in range(n):
        hash[i+1][ord(s[i])-ord('a')]+=1
    
    for i in range(26):
        for j in range(1,n+1):
            hash[j][i] += hash[j-1][i]
            
    while q:
        q-=1
        l,r = map(int,input().split())
            
        oddcount = 0
        
        for i in range(26):
            chatCT = hash[r][i] - hash[l-1][i]
            if chatCT%2!=0:
                oddcount +=1
        if oddcount>1:
            print("NO")
        else:
            print("YES")
            
# time complexity : 0()
# 0(t*q*n) = 10 * 10^5 * 10^5
