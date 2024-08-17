# problem link and logic for solution : http://nayeemmollickjoy.blogspot.com/2017/07/cequ-crucial-equation-spoj-problem.html

def gcd(a, b):
    if b == 0 or a == 0:
        return 0
    if b % a == 0:
        return a
    else:
        return gcd(b % a, a)

def main():
    T = int(input())
    
    for i in range(1, T + 1):
        a, b, c = map(int, input().split())
        g = gcd(a, b)
        
        if c % g == 0:
            print(f"Case {i}: Yes")
        else:
            print(f"Case {i}: No")

if __name__ == "__main__":
    main()
