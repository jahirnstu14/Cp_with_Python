strings = input("Enter the string that length is found by python : ")
length = 0

for _ in strings:
    length+=1

print(f"the lenght of string without build in function {length}")

print(f"using built in function find the lenth of string {len(strings)}")