# English blog : https://cp-algorithms.com/algebra/fibonacci-numbers.html
# time complexity : 0(n)

def fib(n):
    a = 0
    b = 1
    for i in range(n):
        tmp = a + b
        a = b
        b = tmp
    return a

# Taking input from the user
n = int(input("Enter the value of n: "))
print(f"The {n}-th Fibonacci number is {fib(n)}")

# using matrix where time complexity 0(log(n))

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __mul__(self, other):
        # Matrix multiplication
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = 0
                for k in range(2):
                    c[i][j] += self.mat[i][k] * other.mat[k][j]
        return Matrix(c)

def matpow(base, n):
    ans = Matrix([[1, 0], [0, 1]])  # Identity matrix
    while n:
        if n & 1:
            ans = ans * base
        base = base * base
        n >>= 1
    return ans

def fib(n):
    base = Matrix([[1, 1], [1, 0]])
    return matpow(base, n).mat[0][1]

# Example usage
n = int(input("Enter the value of n: "))
print(f"The {n}-th Fibonacci number is {fib(n)}")


