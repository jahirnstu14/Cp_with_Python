# problem logic and problem link: https://lightoj.com/problem/number-sequence

def multi(a, b, mod):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = 0
            for k in range(2):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % mod
    return result

def exponentiation(z, n, mod):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = multi(result, z, mod)
        z = multi(z, z, mod)
        n //= 2
    return result

def find_f_n(a, b, n, m):
    mod = 10**m

    if n == 0:
        return a % mod
    elif n == 1:
        return b % mod

    z = [[1, 1], [1, 0]]
    result = exponentiation(z, n - 1, mod)
    f_n = (result[0][0] * b + result[0][1] * a) % mod

    return f_n

def main():
    t = int(input().strip())

    results = []
    for cs in range(1, t + 1):
        a, b, n, m = map(int, input().strip().split())

        result = find_f_n(a, b, n, m)
        results.append(f"Case {cs}: {result}")

    for res in results:
        print(res)

if __name__ == "__main__":
    main()

