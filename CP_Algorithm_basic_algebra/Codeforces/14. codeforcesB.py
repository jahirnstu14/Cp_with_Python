# problem link : https://codeforces.com/problemset/problem/32/B

# s = input()
# s = s.replace('--','2').replace('-.','1').replace('.','0')
# print(s)

# another way :

a = input()
ans = ''
i = 0
while i < len(a):
    if a[i]=='-' and a[i+1]== '-':
        ans +='2'
        i+=1
    elif a[i]=='-' and a[i+1]== '.':
        ans +='1'
        i+=1
    else:
        ans +='0'
    i+=1
print(ans)