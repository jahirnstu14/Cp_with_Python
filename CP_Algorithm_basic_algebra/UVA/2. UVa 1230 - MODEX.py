def binpow(a, b, m):
    a %= m
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

def main():
    c = int(input("Enter the number of datasets: "))
    
    results = []
    for _ in range(c):
        x, n, m = map(int, input("Enter x, n, m: ").split())
        result = binpow(x, n, m)
        results.append(result)
    
    for result in results:
        print(result)
# where x is base, n is power, m is modular

if __name__ == "__main__":
    main()
