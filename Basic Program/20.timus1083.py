n,s = map(str,input("Enter the number and factorial sign !!!").split())
ln = len(s)
n = int(n)
        
fact=1
for i in range(n,1,-ln):
    fact*=i
print(fact)

