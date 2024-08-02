# https://leetcode.com/problems/binary-search/
# post for many important leetcode binary related problems : https://leetcode.com/problems/koko-eating-bananas/discuss/769702/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.


def binarySearch(array, low, high, searching_value):
    
    while low<=high:
        mid = (low + high)//2 # alernatively we can write low + (high - low)//2
        
        if array[mid] == searching_value:
            return mid
        elif searching_value > array[mid]:
            low = mid+1
        else:
            high = mid -1
            
    return -1
    

# Driver Code
if __name__ == '__main__':
    array  = list(map(int,input().split()))
    searching_value  = int(input())
    
    # Function call
    result = binarySearch(array, 0, len(array)-1, searching_value)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element i s not present in array")