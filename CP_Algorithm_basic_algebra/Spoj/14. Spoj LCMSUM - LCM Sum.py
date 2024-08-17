# logic no 1: https://forthright48.com/spoj-lcmsum-lcm-sum/
# logic no 2 : https://www.tushers.com/spoj-lcm-sum-solution/      . this link also see the number of divisor which is determined.

def precal(n):
    phi = list(range(n + 1))
    res = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] //= i
                phi[j] *= (i - 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            res[j] += i * phi[i]
    
    return res

def main():
    MAXN = 1000000
    res = precal(MAXN)
    
    kase = int(input().strip())
    
    for _ in range(kase):
        n = int(input().strip())
        ans = res[n] + 1
        ans *= n
        ans //= 2
        print(ans)

if __name__ == "__main__":
    main()
