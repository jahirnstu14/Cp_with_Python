string1 = input("Enter the first string : ")
string2 = input("Enter the seconde string : ")

concatednated_string = string1 + string2

print(f"the concatenated string is {concatednated_string}");


# without built in function 

joining_string=""

for s1 in string1:
    joining_string+=s1
for s2 in string2:
    joining_string+=s2
    
print(f"The joining string is {joining_string}")
