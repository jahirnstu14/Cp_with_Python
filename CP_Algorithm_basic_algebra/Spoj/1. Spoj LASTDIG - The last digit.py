# https://www.spoj.com/problems/LASTDIG/

def mod_exp(base, power, mod):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        power //= 2
    return result

def main():
    t = int(input().strip())
    
    for _ in range(t):
        a, b = map(int, input().strip().split())
        print(mod_exp(a, b, 10))

if __name__ == "__main__":
    main()
