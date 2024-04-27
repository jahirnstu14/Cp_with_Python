a = int(input("the first number is :"))
b = int(input("the second  number is :"))
c = int(input("the third   number is :"))

if a>b and a>c:
    print(f"a is the largest value : {a}");
elif b>a and b>c:
    print(f"b is the largest value :{b}");
else :
    print(f"c is the largest value :{c}");
    
# using max function 
maximum = max(a,b,c) 
print(f"the largest number among the {a},{b},{c} is {maximum}");

    