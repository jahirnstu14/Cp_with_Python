# problme link : https://csacademy.com/contest/archive/task/gcd/
# nice blog for knowing the different logic of GCD: https://codeforces.com/topic/46678/diff/en2/en3?locale=ru

# we derived it right and this even reduces our computations now↵
#     So, gcd(a,b)=gcd(b,r) , r is the remainder of the this equation

# nice number theory : https://progkriya.org/gyan/basic-number-theory 
    
def gcd(a,b):
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)

a, b = map(int,input().split())
greatest_common_divisor = gcd(a,b)
print(greatest_common_divisor)


# easy code for gcd

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}.")


# for least common multiple (LCM)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage
if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    gcd_result = gcd(num1, num2)
    lcm_result = lcm(num1, num2)

    print(f"The GCD of {num1} and {num2} is {gcd_result}.")
    print(f"The LCM of {num1} and {num2} is {lcm_result}.")


