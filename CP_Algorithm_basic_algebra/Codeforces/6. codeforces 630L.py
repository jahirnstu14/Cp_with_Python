# problem link : https://codeforces.com/contest/630/problem/L
# solution : https://codeforces.com/blog/entry/24160

# one solution :

n = input()
n = str(int(n[0] + n[2] + n[4] + n[3] + n[1]) ** 5 )
print(n[-5:])


# another beautiful solution 

a = [''] * 6
for i in range(1,6):
    a[i] = input()
    
c = [] * 6

for i in range(1,6):
    c[i] = int(a[i])
    
x = c[1] * 10000 + c[3] * 1000 + c[5] * 100 + c[4] * 10 + c[2] * 1

mul = 1

for _ in range(5):
    mul *=x
    mul %= 100000

print(f"{mul:05d}")

