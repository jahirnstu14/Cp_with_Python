
n = int(input("Enter the n number : "))

b=[bin(i).count('1') for i in range(0,n+1)]
print(b)




# for another solution we can write 

# n&(n-1) drops the lowest set bit and n&1 drop the last bit of binary number 

