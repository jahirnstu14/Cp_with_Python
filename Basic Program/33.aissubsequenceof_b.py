
print("//without built in function//")
a = input("Enter the string a : ")
b = input("Enter the string b : ")

a_index = 0
b_index = 0

while a_index<len(a) and b_index<len(b):
    if a[a_index]==b[b_index]:
        b_index+=1
    a_index+=1

if b_index==len(b):
    print(f"{b} is subsequence of {a}")
else:
    print(f"{b} is not subsequence of {a}")
    

    