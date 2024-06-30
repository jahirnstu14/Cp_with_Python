# to know details about it : https://hellohasan.com/2016/09/25/%e0%a6%95%e0%a6%be%e0%a6%89%e0%a6%a8%e0%a7%8d%e0%a6%9f%e0%a6%bf%e0%a6%82-%e0%a6%b8%e0%a6%b0%e0%a7%8d%e0%a6%9f-counting-sort-algorithm/

# with example : https://www.geeksforgeeks.org/counting-sort/

array = list(map(int,input().split()))
maximum = max(array)
count = [0] * (maximum + 1)

for num in array: 
    count[num]+=1
    
for i in range(1,len(count)):
    count[i] += count[i-1]
    
output = [0] * len(array)

for num in reversed(array):
    output[count[num] - 1] = num
    count[num] -=1
print(output)

# worse time complexxity : 0(N) and space complexity = (size of count arrary(m) + size of output array (n)) because , they are two extra array space 
    
