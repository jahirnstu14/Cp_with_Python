s1 = input("Enter the first string :")
s2 = input("Enter the second string :")

smallerstring = min(s1,s2)
print(f"The smaller string is {smallerstring}")

# without build in function

len1 =len(s1)
len2 =len(s2)

length = min(s1,s2)

for i in range(len(length)):
    if s1[i]<s2[i]:
        lexically_smaller = s1
        break
    elif s1[i]>s2[i]:
        lexically_smaller= s2
        break
    
else:
    if len1<=len2:
        lexically_smaller =s1
    else:
        lexically_smaller = s2
print("The lexigraphically smaller string is {lexically_smaller}")