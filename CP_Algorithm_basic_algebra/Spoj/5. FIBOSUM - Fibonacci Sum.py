# logic link : https://blog.csdn.net/philpanic9/article/details/89104058

MOD = 1000000007

def mul(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
    for i in range(2):
        for j in range(2):
            a[i][j] = res[i][j]

def power(n):
    fib = [[1, 1], [1, 0]]
    temp = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            mul(temp, fib)
        mul(fib, fib)
        n >>= 1
    return temp[0][1]

def main():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        result = (power(r + 2) - power(l + 1) + MOD) % MOD
        print(result)

if __name__ == "__main__":
    main()
