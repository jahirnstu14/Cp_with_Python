# problem logic link : https://www.cnblogs.com/a719525932/p/7691723.html
# to find the one solution of ax + by = c , we know that ax + by = gcd(a,b) , if C is the multiple of gcd(a,b), then, ax + by =c  has solution .
# if c = 1 or multiple of gcd(a,b), then it is possible to find the solution of this equation 

# def extended_gcd(a, b):
#     if b == 0:
#         return a, 1, 0  # gcd(a, b), x, y where a*x + b*y = gcd(a, b)
#     gcd, x1, y1 = extended_gcd(b, a % b)
#     x = y1
#     y = x1 - (a // b) * y1
#     return gcd, x, y

# def find_one_solution(A, B, C):
#     gcd, x0, y0 = extended_gcd(A, B)
#     if C % gcd != 0:
#         return None  # No solution exists if C is not divisible by gcd(A, B)
    
#     # Scale the solution (x0, y0) to be a solution to Ax + By = C
#     x0 *= C // gcd
#     y0 *= C // gcd
    
#     return x0, y0

# # Example usage
# A, B, C = map(int, input("Enter values for A, B, C: ").split())

# solution = find_one_solution(A, B, C)
# if solution:
#     x, y = solution
#     print(f"A solution to {A}x + {B}y = {C} is x = {x}, y = {y}")
# else:
#     print("No solution exists")


# to find number of solution exist  solution 

# import math

# def extended_gcd(a, b):
#     if b == 0:
#         return a, 1, 0
#     d, x1, y1 = extended_gcd(b, a % b)
#     x = y1
#     y = x1 - (a // b) * y1
#     return d, x, y

# def find_one_solution(A, B, C):
#     d, x0, y0 = extended_gcd(A, B)
#     if C % d != 0:
#         return None  # No solution exists if C is not divisible by gcd(A, B)
    
#     x0 *= C // d
#     y0 *= C // d
#     return x0, y0, d

# def find_multiple_solutions(A, B, C, x_min, x_max, y_min, y_max):
#     solution = find_one_solution(A, B, C)
#     if solution is None:
#         return 0
    
#     x0, y0, d = solution
#     g = math.gcd(A, B)
#     a = B // g
#     b = A // g
    
#     def shift_solution(x, y, a, b, count):
#         x += count * b
#         y -= count * a
    
#     # Find t_min and t_max
#     if a != 0:
#         t_min = math.ceil((x_min - x0) / a)
#         t_max = math.floor((x_max - x0) / a)
#     else:
#         t_min = -float('inf')
#         t_max = float('inf')
    
#     if b != 0:
#         t_min_y = math.ceil((y0 - y_max) / b)
#         t_max_y = math.floor((y0 - y_min) / b)
#         t_min = max(t_min, t_min_y)
#         t_max = min(t_max, t_max_y)
#     else:
#         if not (y_min <= y0 <= y_max):
#             return 0

#     if t_min > t_max:
#         return 0

#     return t_max - t_min + 1

# def main():
#     A = int(input("Enter value for A: "))
#     B = int(input("Enter value for B: "))
#     C = int(input("Enter value for C: "))
#     x_min = int(input("Enter minimum value for x: "))
#     x_max = int(input("Enter maximum value for x: "))
#     y_min = int(input("Enter minimum value for y: "))
#     y_max = int(input("Enter maximum value for y: "))
    
#     result = find_multiple_solutions(A, B, C, x_min, x_max, y_min, y_max)
#     print(f"Number of solutions: {result}")

# if __name__ == "__main__":
#     main()

# to find the pair number  of solution 

import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y

def find_one_solution(A, B, C):
    d, x0, y0 = extended_gcd(A, B)
    if C % d != 0:
        return None  # No solution exists if C is not divisible by gcd(A, B)
    
    x0 *= C // d
    y0 *= C // d
    return x0, y0, d

def find_multiple_pairs(A, B, C, x_min, x_max, y_min, y_max):
    solution = find_one_solution(A, B, C)
    if solution is None:
        return []  # No solution exists
    
    x0, y0, d = solution
    g = math.gcd(A, B)
    a = B // g
    b = A // g
    
    pairs = []
    
    def shift_solution(x, y, a, b, count):
        x += count * b
        y -= count * a

    # Find t_min and t_max for x
    if a != 0:
        t_min_x = math.ceil((x_min - x0) / a)
        t_max_x = math.floor((x_max - x0) / a)
    else:
        t_min_x = -float('inf')
        t_max_x = float('inf')
    
    # Find t_min and t_max for y
    if b != 0:
        t_min_y = math.ceil((y0 - y_max) / b)
        t_max_y = math.floor((y0 - y_min) / b)
    else:
        t_min_y = -float('inf')
        t_max_y = float('inf')

    t_min = max(t_min_x, t_min_y)
    t_max = min(t_max_x, t_max_y)

    # Generate valid (x, y) pairs
    for t in range(t_min, t_max + 1):
        x = x0 + t * a
        y = y0 - t * b
        if x_min <= x <= x_max and y_min <= y <= y_max:
            pairs.append((x, y))

    return pairs

def main():
    # Read input values
    A, B, C = 84, 23, 1
    x_min, x_max, y_min, y_max = -10, 10, -10, 12
    
    pairs = find_multiple_pairs(A, B, C, x_min, x_max, y_min, y_max)
    
    if pairs:
        print("Pairs (x, y) satisfying the equation:")
        for (x, y) in pairs:
            print(f"x = {x}, y = {y}")
    else:
        print("No valid pairs found")

if __name__ == "__main__":
    main()
