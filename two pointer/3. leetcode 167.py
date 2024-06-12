# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

numbers = list(map(int,input().split()))
target = int(input())

start = 0
end = len(numbers)-1

while start<end:
    if numbers[start] + numbers[end] == target:
        print(f"{start+1} and {end+1}")
        break
    elif numbers[start] + numbers[end] > target:
        end-=1
    else:
        start+=1

        