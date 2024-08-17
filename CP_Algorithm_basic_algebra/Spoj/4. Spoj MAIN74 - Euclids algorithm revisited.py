# problem solution : https://spoj-sus.blogspot.com/2015/08/main74.html
MOD = 1000000007

def multiply(F, M):
    x = (F[0][0] * M[0][0] % MOD + F[0][1] * M[1][0] % MOD) % MOD
    y = (F[0][0] * M[0][1] % MOD + F[0][1] * M[1][1] % MOD) % MOD
    z = (F[1][0] * M[0][0] % MOD + F[1][1] * M[1][0] % MOD) % MOD
    w = (F[1][0] * M[0][1] % MOD + F[1][1] * M[1][1] % MOD) % MOD

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1],
         [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if n % 2 != 0:
        multiply(F, M)

def fib(n):
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 0:
            print("0")
        elif n == 1:
            print("2")
        else:
            print(fib(n + 3) % MOD)

if __name__ == "__main__":
    main()
