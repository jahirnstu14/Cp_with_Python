# https://takeuforward.org/data-structure/set-matrix-zero/   for brute force/better/optimal solution 

# brute force appraoch
# def rowmark(matrix,n,m,i):
#     for j in range(m):
#         if matrix[i][j]!=0:
#             matrix[i][j]=-1
            
# def colmark(matrix,n,m,j):
#     for i in range(n):
#         if matrix[i][j]!=0:
#             matrix[i][j]=-1

# def zeroMatrix(matrix,n,m):
#     for i in range(n): #N
#         for j in range(m):#M
#             if matrix[i][j] ==0:
#                 rowmark(matrix,n,m,i)#N
#                 colmark(matrix,n,m,j)#M. SO,# Time Complexity: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
                
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] ==-1:
#                 matrix[i][j] = 0
#     return matrix
               

# if __name__ == "__main__":
# 	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 	n = len(matrix)
# 	m = len(matrix[0])
# 	ans = zeroMatrix(matrix, n, m)
 
# more better apprach

# n = len(matrix)
# m = len(matrix[0])

# extrarow = [0] * n
# extracol = [0] * m

# for i in range(n):          
#     for j in range(m):
        # if matrix[i][j]==0:  acceptable solution :
#             row[i]=1
#             col[j]=1
            
# for i in range(n):
#     for j in range(m):
#         if row[i] or col[j]:
#             matrix[i][j]=0
            
# return matrix

# for above problem :
# Complexity Analysis
# Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
# Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

# Space Complexity: O(N) + O(M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
# Reason: O(N) is for using the row array and O(M) is for using the col array.

































 
 
 
 
 
 