# how many 2 divides any number like 100
n = int(input("Enter the integer number : "))
count = 0

while(n%2==0):
    n/=2
    count+=1
print(count)


    
    