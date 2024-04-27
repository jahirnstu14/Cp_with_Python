# 1^1+2^2+3^3+....+n^n
num = int(input("Enter the number upto sum : "))
summation=0
for i in range(1,num+1):
	summation+=i**i
print(summation)