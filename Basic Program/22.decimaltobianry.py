decimalnumber = int(input("Enter the decimal number : "))

if decimalnumber==0:
    print(0)

binary_digit=[]

current_number = abs(decimalnumber)

while current_number>0:
    remainder=current_number%2
    binary_digit.append(str(remainder))
    current_number//=2
    
# binary_digit.reverse()
# binary_string=''.join(binary_digit)
# if decimalnumber<0:
#     binary_string='-'+binary_string
    
# print(f"binary to decimal converter from {decimalnumber} to {binary_string}")

# without join function 
binary_str=''
for i in reversed(binary_digit):
    binary_str+=i
print(binary_str)
    
    
    