
# using hashmap in easy method

n = int(input())
# hashmap = {}

# while n!=1:
#     if n not in hashmap:
#         hashmap[n] = 1
#     else:
#         print(False)
#         break
    
#     sum = 0
    
#     while n:
#         digit = n%10
#         sum+=digit * digit
#         n//=10
#     n = sum
# print(True)


# find same thing using floy's cycle detection algorithm.

def square_of_digit(n):
    sum = 0
        
    while n:
        digit = n%10
        sum+=digit * digit
        n//=10
    return sum

slow=fast=n
while slow!=fast:
    slow = square_of_digit(n)
    fast = square_of_digit(square_of_digit(n))
    
    if slow==fast:
        break
print(slow==1)
    






















