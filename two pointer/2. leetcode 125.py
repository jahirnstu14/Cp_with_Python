# join function is used after convert the string into list using split function . res = "".join(string1.split())
# replace function is used to remove specific character from a string 

# s = input()
# newstring=""

# for str1 in s:
#     if str1.isalnum():          #//isalnum() is used to check the string is alpha or number . if alphabet or number is return 1 or not 1 
#         newstring+=str1.lower()
# if newstring == newstring[::-1]:
#     print(True)
# else:
#     print(False)
        
# manually alphanumberical function :

# if ord('A')<=ord(str1)<=ord('Z') or ord('a')<=ord(str1)<=ord('z') or ord('0')<=ord(str1)<=ord('9'):
#     return 1
# else:
#     return 0

# same thing using two pointer 


s = input()
start = 0
end = len(s)-1

while start<=end:
    if not s[start].isalnum():
        start+=1
        continue
    if not s[end].isalnum():
        end-=1
        continue
    if s[start].lower() != s[end].lower():
        print("False")
    else:
        start+=1
        end-=1
print(True)
       

