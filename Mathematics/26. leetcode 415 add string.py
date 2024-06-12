# important program for large value of two number 


num1 = input()
num2 = input()

i,j = len(num1)-1 , len(num2)-1
carry = 0
res = []

while i>=0 or j>=0 or carry:
    sum = 0 
    if i>=0:
        sum+=int(num1[i])
        i-=1
    if j>=0:
        sum+=int(num2[j])
        j-=1
    
    sum+=carry
    carry = sum // 10
    res.append(str(sum%10))
res.reverse()
res= ''.join(res)
print(res)
        