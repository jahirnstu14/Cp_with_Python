# problem link : https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1045
# logic behind exculid gcd : https://returnzerooo.wordpress.com/2017/08/12/%E0%A6%8F%E0%A6%95%E0%A7%8D%E0%A6%B8%E0%A6%9F%E0%A7%87%E0%A6%A8%E0%A7%8D%E0%A6%A1%E0%A7%87%E0%A6%A1-%E0%A6%87%E0%A6%89%E0%A6%95%E0%A7%8D%E0%A6%B2%E0%A6%BF%E0%A6%A1%E0%A7%80%E0%A7%9F%E0%A6%BE%E0%A6%A8/


# for modulus inverse
# ax + by = 1 = gcd(a,b)
# 84*(-3) + 23*11 = 1, a=84,b=23,x=-3,y=11 

# we know that , b * b^-1 = 1

# যেকোন a, b এর ক্ষেত্রেই এরকমভাবে x, y এর মান বের করা যাবে। কিন্তু এই উদাহরণের a, b এর একটা আলাদা বৈশিষ্ট্য আছে, এরা কো-প্রাইম। অর্থাৎ ১ ছাড়া অন্য কোন সংখ্যা দ্বারা a,b উভয়েই নিঃশেষে বিভাজ্য নয়। এক্ষেত্রে, x হচ্ছে a modulo b এর multiplicative inverse,  y হল b modulo a এর multiplicative inverse.
# অর্থাৎ, x^-1 = a%b, y^-1 = b%a. ক্যালকুলেশনের সুবিধার্থে অনেক ক্ষেত্রে x, y এর মান পজিটিভ হয়ে থাকে।
# উপরের উদাহরণে, (-3) % 23 = 20, 11 % 84 = 11
 
# 20^-1 = 84 % 23    -> 84*20 = 1680%23 = 1
# 11^1 = 23%84      -> 23*11 = 253%84  = 1

# def extended_euclid(a, b):
#     if b == 0:
#         return a, 1, 0
#     gcd, x1, y1 = extended_euclid(b, a % b)
#     x = y1
#     y = x1 - (a // b) * y1
#     return gcd, x, y

# if __name__ == "__main__":
#     while True:
#         try:
#             a, b = map(int, input().split())
#             gcd, x, y = extended_euclid(a, b)
#             print(f"{x} {y} {gcd}")
#         except EOFError:
#             break
# it is the simple eculiclid algorithm 
# another same way 

# recursive function for this . here c = 1

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
    
    
# optional solve for find x0,yo . it is same like above but here c has aribitary value

def gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = gcd(b, a % b)
    x = y1
    y = x1 - y1 * (a // b)
    return d, x, y

def find_any_solution(a, b, c):
    g, x0, y0 = gcd(abs(a), abs(b))
    if c % g != 0:
        return False, None, None, None
    
    x0 *= c // g
    y0 *= c // g
    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0
    return True, x0, y0, g

def main():
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = int(input("Enter value for c: "))
    
    found, x0, y0, g = find_any_solution(a, b, c)
    if found:
        print(f"Solution found: x0 = {x0}, y0 = {y0}, gcd = {g}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
