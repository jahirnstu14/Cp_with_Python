# 1-2+3-4....+n
num = int(input("Enter the number upto sum : "))
summation=0
sign=1
for i in range(1,num+1):
	summation+=sign**i
	sign=-sign
print(summation)