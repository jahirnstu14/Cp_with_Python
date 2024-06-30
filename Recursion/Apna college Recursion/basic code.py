# apna college link : https://www.youtube.com/watch?v=5Boqfjissv0&list=LL

# print n to 1 using recursion 

# def printnumber(n):
#     if n == 0:
#         return
#     print(n)
#     printnumber(n-1)



# n = int(input())
# printnumber(n)

# 1 to n (5) print using recursion 

# def printnumber(n):
#     if n == 6:
#         return
#     print(n)
#     printnumber(n+1)

# n = int(input())
# printnumber(n)

# print sum first n  natural number using recursion   1+2+3+4+5+6+7+......+n

# def numbersum(i, n, sum):
#     if i == n:
#         sum += i
#         print(sum)
#         return
#     sum += i
#     numbersum(i+1, n, sum)

# n = int(input()) # sum upto n . if n =5 , then , 1+2+3+4+5 = 15
# numbersum(1, n, 0) # function call


# after changing after recursion call
# recursion call upore ja thakbe ta stack nichhe theke shruru habe . ar nichher statement upor theke shuru habe stack er . 

# def numbersum(i, n, sum):
#     if i == n:
#         sum += i
#         print(sum)
#         return
#     sum += i
#     numbersum(i+1, n, sum) # recursion call
#     print(i)


# n = int(input()) # sum upto n . if n =5 , then , 1+2+3+4+5 = 15
# numbersum(1, n, 0) # function call

# calculate factorial upto n 

# def numberfactorial(n):
#     if n==0 or n==1:
#         return 1
#     fact_nmu1 = numberfactorial(n-1) # recursion call
#     fact = n * fact_nmu1
#     print(fact)
#     return fact
    

# n = int(input()) # sum upto n . if n =5 , then , 1+2+3+4+5 = 15
# ans = numberfactorial(n) # function call
# print(ans)

# fact_nmu1 = numberfactorial(n-1) # recursion call
#     fact = n * fact_nmu1
#     return fact   
# above three line can be written as return n * numberfactorial(n-1)


# print fibonaaci series using recursion method 


# def fibnaacinumber(a, b, n):
#     if n ==0:
#         return
#     c =  a + b
#     print(c)
#     fibnaacinumber(b, c, n-1)


# a , b = 0, 1
# print(a)
# print(b)
# n = int(input("Enter the nth number : "))
# fibnaacinumber(a, b, n-2)

# recursion er basic condition three : for x^n
    
# 1. function ki deya habe x,n
# 2. ki kaj karte habe x ^n = (x * x^(n-1))
# 3. base case : n = = 0 will be 1 and x = 0 will be 0 . recusion will return 0 . 

# above three codition will be for all types of recursion problem 

# calculate x^n using recursion 

# def printxtopowern(x, n):
#     if n==0: base case : 1
#         return 1
#     if x == 0: base case : 2
#         return 0
    
    
#     num1 = printxtopowern(x, n-1) ki kaj karte habe. 
#     powern = x * num1
#     return powern

# x, n = map(int, input().split()) #x =2, n= 5

# printxtopowern(x, n)

#  num1 = printxtopowern(x, n-1)
#     powern = x * num1
#     return powern

# above three line can be written return x * printxtopowern(x, n-1)

# calculate x^n using recursion (with logn )

def printxtopowern(x, n):
    if n==0: #base case : 1
        return 1
    if x == 0: #base case : 2
        return 0
    
    if n%2 == 0: # power n  is equal to even
        return printxtopowern(x, n//2) * printxtopowern(x, n//2)
    else:
        return printxtopowern(x, n//2) * printxtopowern(x, n//2) * x

x, n = map(int, input().split()) #x =2, n= 5

ans = printxtopowern(x, n)
print(ans)

# above program : Detailed Step-by-Step Execution for x = 2 and n = 5
# printxtopowern(2, 5)
# n is odd, so it calculates printxtopowern(2, 2) * printxtopowern(2, 2) * 2.
# printxtopowern(2, 2)
# n is even, so it calculates printxtopowern(2, 1) * printxtopowern(2, 1).
# printxtopowern(2, 1)
# n is odd, so it calculates printxtopowern(2, 0) * printxtopowern(2, 0) * 2.
# printxtopowern(2, 0)
# n is 0, so it returns 1.
# Putting it all together:

# printxtopowern(2, 0) returns 1.
# printxtopowern(2, 1) is 1 * 1 * 2 = 2.
# printxtopowern(2, 2) is 2 * 2 = 4.
# printxtopowern(2, 5) is 4 * 4 * 2 = 32.
# So, the output for x = 2 and n = 5 is 32.


def binary_search_recursive(arr, target, low, high):
    if low > high:  # Base case: target is not found
        return -1
    
    mid = (low + high) // 2  # Calculate the middle index
    
    if arr[mid] == target:  # Target is found
        return mid
    elif arr[mid] > target:  # Target is in the left half
        return binary_search_recursive(arr, target, low, mid - 1)
    else:  # Target is in the right half
        return binary_search_recursive(arr, target, mid + 1, high)

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Element {target} is at index {result}")


# void foo(int n)
# {
#     // Base case
#     if(n < 1) return;
#     // Recursive case
#     foo(n-1);
#     foo(n-2);
# }
# এখানে আমরা দুটো রিকার্সিভ কল করছি। একবার n-1 দিয়ে, আরেকবার n-2 দিয়ে। এখানে ফাংশন কলটা একটা ট্রি এর মত করে আগাবে। যদি আমরা 5 দিয়ে ফাংশনটা কল করি তাহলে এরকম হবে।

#                          foo(5)
#                   /                 \
#                  /                   \
#            foo(4)                     foo(3)
#          /       \                  /        \
#     foo(3)       foo(2)        foo(2)         foo(1)
#     /    \       /    \        /    \         /    \
# foo(2) foo(1) foo(1) foo(0) foo(1) foo(0) foo(0) foo(-1)

# most important video to understand multiple recursion : https://www.youtube.com/watch?v=kvRjNm4rVBE





