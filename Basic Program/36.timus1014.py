number = int(input("Enter the integer number : "))

result = ""

if number==0:
    print(10)
elif number==1:
    print(number)

else:
    i=9
    while i>=2:
        while number%i==0:
            result+=str(i)
            number/=i
        i-=1
    if number==1:
        print(result)
    else:
        print(-1)
