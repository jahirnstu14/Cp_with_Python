# https://leetcode.com/problems/container-with-most-water/

height =  list(map(int,input().split()))

start , end = 0 , len(height)-1
water = 0

while start < end:
    
    current_water = (end-start) * min(height[start] ,height[end])
    water = max(water,current_water)
    
    if height[start]<height[end]:
        start+=1
        
    else:
        end-=1

print(water)