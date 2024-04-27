character = input("Enter string of : ")
upper =0
lower = 0

for char in character:
    if char.isupper():
        upper+=1
        
    elif char.lower():
        lower+=1
        
print(f"the number of uppercase {upper} and number of lowercase is {lower}");

# without built in function 

count_upper=0
count_lower=0
for char in character:
        # Check if the character is an uppercase letter by comparing its ASCII value directly
        if 'A' <= char <= 'Z':
            count_upper += 1
        # Check if the character is a lowercase letter by comparing its ASCII value directly
        elif 'a' <= char <= 'z':
            count_lower += 1
        
print(f"the upper is {count_upper} and the lower number is {count_lower}")
