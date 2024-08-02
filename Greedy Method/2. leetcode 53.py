# nice solution with brute force and optimal solution and  Kadane's Algorithm : Maximum Subarray Sum in an Array  and link is : https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/

# brute force method
# minimum subarray maximum er ulta habe . same procedure only conditional operation change habe. 

# nice problem :
def max_subarray_sum(arr):
    n = len(arr)
    maximum = float('-inf')
    
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i, j+1):
                sum += arr[k]
            
            maximum = max(maximum, sum) # for minimum subarray we can write , minimum = float('inf') and minimum = min(minimu, sum)
    return maximum
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(arr)
    print("The maximum subarray sum is:", max_sum)
    

    
# Time Complexity: O(N3), where N = size of the array.
# Reason: We are using three nested loops, each running approximately N times.
# Space Complexity: O(1) as we are not using any extra space.

# better approach 

def max_subarray_sum(arr):
    n = len(arr)
    maximum = float('-inf')
    
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            maximum = max(maximum, sum)
    return maximum
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(arr)
    print("The maximum subarray sum is:", max_sum)

# Time Complexity: O(N2), where N = size of the array.
# Reason: We are using two nested loops, each running approximately N times.
# Space Complexity: O(1) as we are not using any extra space.


# most optimal solution using kadan's algorithm 

def max_subarray_sum(arr):
    maximum = float('-inf')
    sum = 0
    
    for num in arr:
        sum += num
        
        if sum > maximum:
            maximum = sum
            
        if sum < 0:
            sum = 0
    
    return maximum
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(arr)
    print("The maximum subarray sum is:", max_sum)
    
# Time Complexity: O(N), where N = size of the array.
# Reason: We are using a single loop running N times.
# Space Complexity: O(1) as we are not using any extra space.

# with printing the subarray

def max_subarray_sum(arr):
    maximum = float('-inf')
    sum = 0
    n = len(arr)
    start = 0
    end = 0
    s = 0
    
    for i in range(n):
        sum += arr[i]
        
        if sum > maximum:
            maximum = sum
            start = s
            end = i
        
        if sum < 0:
            sum = 0
            s = i+1
    return maximum , arr[start:end+1]
            
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, subarry = max_subarray_sum(arr)
    print("The maximum subarray sum is:", max_sum)
    print(f"The subarray is : {subarry}")








