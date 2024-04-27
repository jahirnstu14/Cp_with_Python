a = int(input("Enter the year to check leap year or not :"))

if (a%400==0) or (a%100!=0 and a%4==0):
    print(f"{a} is the leap year")

else:
    print(f"{a} is not leap year")
    
    
