
# it is the basic of prime factorization 

def factorization(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        print(f"2^{count}", end=" ")
    
    for i in range(3, int(n**0.5) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            print(f"{i}^{count}", end=" ")
    
    # this condition only for prime number 
    
    if n > 2:
        print(f"{n}^1", end="")

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        factorization(n)
        print()

if __name__ == "__main__":
    main()
