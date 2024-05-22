
n = int(input("Enter the integer : "))
symbol = 1
if n<0:
    n = -n
    symbol =-1
else:
    symbol=1
    
reverse = 0

while n:
    reverse = 10 * reverse + n%10
    n//=10


if reverse>pow(2,31):
    print(0)
else:
    print(reverse * symbol)
    