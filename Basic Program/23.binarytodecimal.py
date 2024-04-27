binary_num = input("Enter the binary number : ")

power = len(binary_num)-1

decimalnumber=0

for digit in binary_num:
    if digit=='1':
        decimalnumber+=2**power
    power-=1
    
print(f"The decimal number is {decimalnumber} for binarynumber {binary_num}")
    
    