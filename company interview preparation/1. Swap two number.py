# without exor function 
# Given two numbers
a = 5
b = 10

# Swapping using arithmetic operations
a = a + b  # a now becomes 15
b = a - b  # b now becomes 5 (original value of a)
a = a - b  # a now becomes 10 (original value of b)

# Output the swapped values
print("After swapping: a =", a, "b =", b)


# with exor functioon 
# Given two numbers
a = 5
b = 10

# Swapping using XOR
a = a ^ b  # Step 1: a becomes a XOR b
b = a ^ b  # Step 2: b becomes a XOR b, which is the original value of a
a = a ^ b  # Step 3: a becomes a XOR b, which is the original value of b

# Output the swapped values
print("After swapping: a =", a, "b =", b)
