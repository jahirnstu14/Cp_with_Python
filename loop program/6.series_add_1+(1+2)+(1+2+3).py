# the series is 1+(1+2)+(1+2+3)+(1+2+3+4+....n)

num = int(input("Enter the last number of the series : "))
sum = 0

for i in range(1,num+1):
    for j in range(1,i+1):
        sum+=j
print(f"The total sum is {sum}");


