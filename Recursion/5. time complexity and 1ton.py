def nto1(n):
    if n==0:
        return
    # return karar projonto ai area cholbe  cholbe be 
    nto1(n-1)
    # return karar por ei area cholbe 
    print(n)

n = int(input())
nto1(n)


# for recursion time complexity we can find 
# number of functions calls ---> n
# each function complexity ---->1
# total complexity will be = n * 1


# for time complexity for recursion will be p^n , where p is the number of times recursion call perform and n means number of call stack .

def recursiveFunction(level):
    if level == 0:
        return
    recursiveFunction(level - 1)
    recursiveFunction(level - 1)

# Initial call to the recursive function
recursiveFunction(3)

# so, the above problem the time complexity 0(2^n) . because, in recursion , function is called in two times. if function called would have been three times , the time complexity would have been 0(3^n) . example :

def recursiveFunction(n):
    if n == 0:
        return 1
    return recursiveFunction(n - 1) + recursiveFunction(n - 1) + recursiveFunction(n - 1)

# Example usage
n = 3
result = recursiveFunction(n)
print(f"Result: {result}")


# in the above program , recursiveFunction called in three times. n denotes the each function call stack  and p denotes  the number of recursion called simultaneously. in the above program, (1+1+1)^n , so , time complexity is 0(3)^n. if we consider tree , it'll have three children for every node. if function calling 4 times then , 4^n . if we consider tree , it'll have four children for every node.

# let, time complexity for recursion p^n . p is the number of recursion or function call and n is the each function called time  complexity.

# example : 

def sumofdigit(n):
    if n==0:
        return 0
    return sumofdigit(n//10)+n%10

    
n = int(input())
print(sumofdigit(n))

# above program, recursion call in 1 times. each function called time complexity is 0(logn) . total time complexity will be 1^logn. so , time complexity is log(n) . 

def sumofdigit(n):
    if n==0:
        return 0
    return sumofdigit(n//10)+n%10 + sumofdigit(n//10)+n%10

    
n = int(input())
print(sumofdigit(n))

# in the above problem , sumofdigit() is called two times . each function complexity is log(n) . so, total time complexity will be 0(2^logn) . 
    

 


