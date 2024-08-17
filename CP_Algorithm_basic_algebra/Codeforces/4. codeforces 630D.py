# problem link : https://codeforces.com/contest/630/problem/D
# discussion : https://codeforces.com/blog/entry/24160

def main():
    n = int(input())
    sum = 0
    for i in range(n + 1):
        sum += 6 * i
    print(sum + 1)

if __name__ == "__main__":
    main()
    
# time limit exceed because , the value of n is higest is 10^9 . and it's complexity is 0(n). so, the code won't execute . complexity must be less than 0(n)

def main():
    n = int(input())
    # The formula to calculate the number of hexagons
    sum = 1 + 3 * n * (n + 1)
    print(sum)

if __name__ == "__main__":
    main()

