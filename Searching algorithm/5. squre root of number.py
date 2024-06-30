eps = 1e-6 #use to determine the number of decimal number needed after decimal point 

n = int(input("Enter a number to find its square root: "))
low = 1  
high = n  # The upper bound is the number itself

while (high - low) > eps:
# while low<=high if  i use this then, while loop will be infinite . 
    mid = (high + low) / 2  # Use division to get a floating-point number
    if (mid * mid) < n: # for cubic root mid * mid * mid <n or any other root to find we only multipy with mid equal to that time . 
        low = mid
    else:
        high = mid

print(f"The square root of {n} is approximately {low:.6f}")
