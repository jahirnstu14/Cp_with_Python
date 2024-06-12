s = input()
k = int(input())

c_frquency = {}
l=0

longest_sub_length = 0
r = 0

for r in range(len(s)):
    if s[r] not in c_frquency:
        c_frquency[s[r]]=0
    c_frquency[s[r]]+=1
    
    cell_count  = r-l+1  # windows count for two sliding windows 
    
    if cell_count - max(c_frquency.values()) <=k:
        longest_sub_length = max(longest_sub_length,cell_count)
    
    
    else:
        c_frquency[s[l]]-=1
        
        if not c_frquency:
            c_frquency.pop(s[l])
        l+=1
print(longest_sub_length)        

