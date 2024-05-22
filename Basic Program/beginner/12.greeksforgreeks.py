
# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

N,X = map(int,input().split())

arr = list(map(int,input().split()))
    
count = 0
    
for i in range(N):
    if arr[i]==X:
        count+=1
    
print(f"{count}")
        
    
    