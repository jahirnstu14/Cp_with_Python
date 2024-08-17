import sys

def normal_sieve(mx):
    # normal sieve O(nloglogn) complexity
    prime = [True] * (mx + 1)  # mark them as true.
    for i in range(2, mx + 1):
        if prime[i]:
            for j in range(i * i, mx + 1, i):
                prime[j] = False
    return prime

def main():
    mx = int(input("Enter the maximum range for sieve: "))  # Use input function to get the maximum range
    prime = normal_sieve(mx)
    cont = 1  # 2 is already counted
    print(2)
    for i in range(3, mx + 1, 2):
        if prime[i]:
            cont += 1
            if cont % 100 == 1:
                print(i)

if __name__ == "__main__":
    main()
