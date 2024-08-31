# problem link : https://codeforces.com/blog/entry/76352

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        n //= 2
        if n % 2 != 0:
            print("NO")
            continue
        print("YES")
        for i in range(1, n + 1):
            print(i * 2, end=" ")
        for i in range(1, n):
            print(i * 2 - 1, end=" ")
        print(3 * n - 1)

if __name__ == "__main__":
    main()
