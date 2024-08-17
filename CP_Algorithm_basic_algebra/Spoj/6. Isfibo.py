# problme slink :https://www.hackerrank.com/challenges/is-fibo/problem

def isFibo(n):
    fibo = []
    a, b = 0, 1
    fibo.append(a)
    for _ in range(1, 101):
        fibo.append(b)
        a, b = b, a + b
    
    if n in fibo:
        return "IsFibo"
    else:
        return "IsNotFibo"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(isFibo(n))

if __name__ == "__main__":
    main()
