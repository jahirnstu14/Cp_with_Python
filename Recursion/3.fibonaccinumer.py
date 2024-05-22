def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2) 
n = int(input())
print(fib(n))



# //  alternative solution using dynamic programming 

list1 = [0, 1]
n = int(input())

for i in range(2, n+1):
    list1.append(list1[i-1] + list1[i-2])
    
print(list1[n])


    