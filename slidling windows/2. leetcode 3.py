s = input()

store = [0] * 256
l =0
r=0
ans = 0

while r<len(s):
    
    store[ord(s[r])]+=1
    
    while store[ord(s[r])] > 1:
        store[ord(s[l])]-=1
        l+=1
        
    ans = max(ans, r-l+1)
    r+=1
print(ans)