inputstring = input("Enter the number using spaces : ")

elements = inputstring.split("")

print("Using comprehensive method :")

list1 = [int(element) for element in elements]
print(list1)


print(" using general loop : ")
list2 = []

for element in elements:
    list2.append(int(element))
    
print(list2)
