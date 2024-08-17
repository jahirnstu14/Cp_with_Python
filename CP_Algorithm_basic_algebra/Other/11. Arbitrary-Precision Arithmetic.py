# Input : 
# To read a long integer, read its notation into a string and then convert it to "digits":
    
# def process_large_number(s):
#     a = []
#     length = len(s)
#     i = length

#     while i > 0:
#         if i < 9:
#             a.append(int(s[:i]))
#         else:
#             a.append(int(s[i-9:i]))
#         i -= 9
    
#     return a

# # Example usage
# s = input().strip()  # Read input as a string
# result = process_large_number(s)
# print(result)

# If the input can contain leading zeros, they can be removed as follows:
# def process_large_number(s):
#     a = []
#     length = len(s)
#     i = length

#     while i > 0:
#         if i < 9:
#             a.append(int(s[:i]))
#         else:
#             a.append(int(s[i-9:i]))
#         i -= 9
    
#     # Remove trailing zeros from the list
#     while len(a) > 1 and a[-1] == 0:
#         a.pop()
    
#     return a

# # Example usage
# s = "000000123456000000"  # Example large number with leading and trailing zeros
# result = process_large_number(s)
# print(result)  # Output will be [123]

# Addition :
# For the addition of two numbers where one number has n digits and the other has m digits, the number of digits .The maximum number of digits in the sum of two numbers can be at most max(n, m)+1 where n is the number of digits in the first number and m is the number of digits in the second number.
# Increment long integer a by b  and store result in a :
# def add_large_numbers(a, b, base=10):
#     # Reverse lists to handle the least significant digits first
#     a.reverse()
#     b.reverse()

#     max_length = max(len(a), len(b))
    
#     # Ensure both lists are of equal length
#     a.extend([0] * (max_length - len(a)))
#     b.extend([0] * (max_length - len(b)))
    
#     result = []
#     carry = 0
    
#     for i in range(max_length):
#         total = a[i] + b[i] + carry
#         result.append(total % base)
#         carry = total // base
    
#     if carry:
#         result.append(carry)
    
#     # Reverse the result to restore original order
#     result.reverse()
    
#     return result

# # Example usage
# a = [9, 9, 9]  # Representing the number 999
# b = [1]        # Representing the number 1

# result = add_large_numbers(a, b)
# print(result)  # Output will be [1, 0, 0, 0], representing the number 1000

# Subtraction :
# Decrement long integer a by b (a>=b) and store result in a :
    
# def subtract_large_numbers(a, b, base=10):
#     # Reverse lists to handle the least significant digits first
#     a = a[::-1]
#     b = b[::-1]
    
#     max_length = max(len(a), len(b))
    
#     # Ensure both lists are of equal length
#     a.extend([0] * (max_length - len(a)))
#     b.extend([0] * (max_length - len(b)))
    
#     result = []
#     borrow = 0
    
#     for i in range(max_length):
#         diff = a[i] - borrow - (b[i] if i < len(b) else 0)
#         if diff < 0:
#             diff += base
#             borrow = 1
#         else:
#             borrow = 0
#         result.append(diff)
    
#     # Remove leading zeros
#     while len(result) > 1 and result[-1] == 0:
#         result.pop()
    
#     # Reverse result to restore original order
#     result = result[::-1]
    
#     return result

# # Example usage
# a = [2, 0, 0]  # Representing the number 200
# b = [1, 0]     # Representing the number 10

# result = subtract_large_numbers(a, b)
# print(result)  # Output will be [1, 9, 0], representing the number 190

# Multiplication by short integer
# Multiply long integer a by short integer b (b< base ) and store result in a  : 
    
# def multiply_large_number_by_small(a, b, base=10):
#     carry = 0
#     result = []
    
#     for digit in a:
#         product = digit * b + carry
#         result.append(product % base)
#         carry = product // base
    
#     if carry > 0:
#         result.append(carry)
    
#     # Remove leading zeros
#     while len(result) > 1 and result[-1] == 0:
#         result.pop()
    
#     return result

# # Example usage
# a = [9, 9, 9]  # Representing the number 999
# b = 7          # Short integer to multiply with

# result = multiply_large_number_by_small(a, b)
# print(result)  # Output will be [3, 9, 9, 6], representing the number 6993

# Multiplication by long integer 
# multiply long integers a and b and stroe result in c:
# For two numbers with n digit and m digits:
# •	The smallest product will have at least n+m-1 digits.
# •	The largest product will have exactly n+m digits

# it can be done using forward loop in another way 

#  using backward loop 

# def multiply_large_integer(a, b, base=10):
#     # Initialize the result array with zeros
#     c = [0] * (len(a) + len(b))
    
#     # Perform the multiplication
#     for i in range(len(a) - 1, -1, -1):
#         carry = 0
#         for j in range(len(b) - 1, -1, -1):
#             cur = c[i + j + 1] + a[i] * b[j] + carry
#             c[i + j + 1] = cur % base
#             carry = cur // base
#         c[i + j] += carry
    
#     # Remove leading zeros
#     while len(c) > 1 and c[0] == 0:
#         c.pop(0)
    
#     return c

# # Example usage:
# a = [1, 2, 3]  # Represents the number 123
# b = [4, 5, 6]  # Represents the number 456
# base = 10

# result = multiply_large_integer(a, b, base)
# print(result)  # Output should represent the number 123 * 456

# Division by short integer
# Divide long integer a by short integer b , store integer result in a and remainder in carry :

# General Formula:
# Quotient Digits: If the dividend has n digits and the divisor has m digits, the quotient will have approximately n-m+1 digits. 
# Remainder Digits: The remainder will have at most m digits.

def divide_large_integer(a, b, base=10):
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        cur = a[i] + carry * base
        a[i] = cur // b
        carry = cur % b
    
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    
    return a, carry

# Example usage:
a = [1, 2, 3]  # Represents the number 123
b = 4
base = 10

result, remainder = divide_large_integer(a, b, base)
print("Quotient:", result)  # Output should represent the quotient of 123 / 4
print("Remainder:", remainder)  # Output should represent the remainder of 123 / 4


    









    










