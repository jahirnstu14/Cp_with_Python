# for details : https://cp-algorithms.com/algebra/extended-euclid-algorithm.html

# Nice bangla explanation for extended gcd : https://iishanto.com/extended-euclidean-algorithm-in-bangla/

def gcd(a, b):
    x, y = 1, 0
    x1, y1 = 0, 1
    a1, b1 = a, b

    while b1:
        q = a1 // b1
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a1, b1 = b1, a1 - q * b1

    return a1, x, y

# Function to take user input and call the gcd function
def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result_gcd, x, y = gcd(a, b)
    print(f"GCD: {result_gcd}, x: {x}, y: {y}")

if __name__ == "__main__":
    main()


# recursive function for this 

def gcd(a, b):
    if b == 0:
        x = 1
        y = 0
        return a, x, y
    else:
        gcd_value, x1, y1 = gcd(b, a % b)
        x = y1
        y = x1 - y1 * (a // b)
        return gcd_value, x, y

# Function to take user input and call the gcd function
def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    gcd_value, x, y = gcd(a, b)
    print(f"GCD: {gcd_value}, x: {x}, y: {y}")

if __name__ == "__main__":
    main()
