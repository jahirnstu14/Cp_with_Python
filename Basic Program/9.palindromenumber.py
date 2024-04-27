n = int(input("enter the interger value :"))
temp=n
reverse=0
while(n>0):
    digit = n%10
    reverse= reverse*10 + digit
    n = n//10
    
#with python default function :
# r = str(n)  
# reverse = r[::-1] 

if(reverse==temp):
    print(f"{temp} is the palidrome number ")
else:
    print(f"{temp} is not palidrome number ")