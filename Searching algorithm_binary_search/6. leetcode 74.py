# Using brtue force method 
n , m = map(int,input().split())
matrix = []
target = int(input())                                                                                                           

# for i in range(n):
#     matrix.append(list(map(int,input().split())))

# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == target:
#             print("target value is found ")
#             break
# print("target value is not found")  # time complexity will be = 0(N*M) AND 0(1)

# better approach is from the above 

# simple code

# def call_binary_function(low,high):
    

# for i in range(n):
#     if matrix[i][0] > target and matrix[i][m-1]:
#         call_binary_function(matrix[i][0],matrix[i][m-1])


# time complexity will be 0(N * log(n*m)) and space comlexity 0(1)

# most efficient approach for the above problem is 

# Use binary search.

# n * m matrix convert to an array => matrix[x][y] => a[x * m + y]

# an array convert to n * m matrix => a[x] =>matrix[x // m][x % m];  

n = len(matrix)
if n == 0:
    print("false")
m = len(matrix[0])
l, r = 0, m * n - 1

while l < r:
    mid = (l + r ) // 2
    if matrix[mid // m][mid % m] < target:
        l = mid + 1
    else:
        r = mid    # the reason behind not having r = mid - 1 beacause, the if condition has only less than sample so, another else condition will be equal or less than one.

print(matrix[r // m][r % m] == target) 

        

    





