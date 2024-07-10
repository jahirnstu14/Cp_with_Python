# Floyd Warshall Algorithm called multisource shortest path algorithm and it also soluton for cycle or negative weight of edges

# nice solution : https://takeuforward.org/data-structure/floyd-warshall-algorithm-g-42/

class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        
        # Initialize matrix: convert -1 to a large number and set diagonals to 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 1e9
                if i == j:
                    matrix[i][j] = 0
        
        # Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        # Post-Processing: convert large number back to -1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1e9:
                    matrix[i][j] = -1

if __name__ == "__main__":
    V = 4
    matrix = [[-1] * V for _ in range(V)]
    
    matrix[0][1] = 2
    matrix[1][0] = 1
    matrix[1][2] = 3
    matrix[3][0] = 3
    matrix[3][1] = 5
    matrix[3][2] = 4

    obj = Solution()
    obj.shortest_distance(matrix)

    for row in matrix:
        print(" ".join(map(str, row)))
