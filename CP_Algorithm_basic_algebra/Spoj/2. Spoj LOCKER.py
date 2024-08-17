# problem link : https://www.spoj.com/problems/LOCKER/
import sys
MOD = 1000000007

def powe(a, b):
    ans = 1
    while b > 0:
        if b % 2:
            ans = (ans * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return ans

def main():
    import time

    t = int(input().strip())
    
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        if n % 3 == 0:
            result = powe(3, n // 3) % MOD
        elif n % 3 == 1:
            if n == 1:
                result = 1
            else:
                result = (powe(3, n // 3 - 1) * 4) % MOD
        else:
            if n == 2:
                result = 2
            else:
                result = (powe(3, n // 3) * 2) % MOD
        
        results.append(result)
    
    for res in results:
        print(res)
    
    # Print time taken for execution
    print(f"Time : {time.process_time()}s", file=sys.stderr)

if __name__ == "__main__":
    main()
