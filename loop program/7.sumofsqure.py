# 1^2+2^2+3^2+....+n^2
num = int(input("Enter the number upto sum : "))
# summation=0
# for i in range(1,num+1):
# 	summation+=i**2
# print(summation)

# another way

summation = sum(i**2 for i in range(1,num+1))
print(summation)