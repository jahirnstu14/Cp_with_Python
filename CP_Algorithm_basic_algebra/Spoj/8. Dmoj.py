# problem link : https://dmoj.ca/problem/fibonacci

MOD = 10**9 + 7

def matrix_multiply(A, B, mod=MOD):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]
    ]

def matrix_power(matrix, n, mod=MOD):
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = matrix
    
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, base, mod)
        base = matrix_multiply(base, base, mod)
        n //= 2
    
    return result

def fibonacci(n, mod=MOD):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    T = [[1, 1], [1, 0]]
    T_n = matrix_power(T, n-1, mod)
    
    return T_n[0][0]

# Reading input
n = int(input().strip())
print(fibonacci(n))
