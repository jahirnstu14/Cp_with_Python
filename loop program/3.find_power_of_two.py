# finds out the highest number power of 2 and less than 1000

n = int(input("enter the integer number : "))

x = 1
high=0
while(5**x<n):
    high=5**x
    x=x+1
    
print(high)

# another solution
x=1
while(x*2<n):
    x=x*2
print(x)

# same thing using for loop
for _ in range(30):
    if x*2>n:
        break
    x*=2
print(x)
    