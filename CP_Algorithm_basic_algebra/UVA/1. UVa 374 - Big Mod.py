def modular_exponentiation(b, p, m):
    ans = 1
    b = b % m
    while p > 0:
        if p & 1:
            ans = (ans * b) % m
        b = (b * b) % m
        p >>= 1
    return ans

def main():
    try:
        while True:
            b = int(input("Enter base (b): "))
            p = int(input("Enter exponent (p): "))
            m = int(input("Enter modulus (m): "))
            result = modular_exponentiation(b, p, m)
            print(result)
    except EOFError:
        return

if __name__ == "__main__":
    main()
