#  without find() or built in function 

# full_text =  input("Enter hte full text : ")
# searching_text = input("Enter the searching text : ")

# count= 0

# for i in range(len(full_text)):
#     if full_text[i:i+len(searching_text)]==searching_text:
#         count+=1
# print(f"the number of times the substring {searching_text} are {count}")

# using find function 
# find function always return the first index value when it find the searching value first . find(substring,start,end) if there is no start,end parameter then it will consider default , if having one it consider start. start mean it searching start upto end the string .if not find return -1 .find gives the return of the index where the substring is find first in the full_text.


full_text = input("Enter the full text: ")
searching_text = input("Enter the searching text: ")
count = 0
start = 0

while start < len(full_text):
    index = full_text.find(searching_text, start)
    if index == -1:
        break
    count += 1
    start = index + 1  
    
print(f"The number of times the substring '{searching_text}' occurs is {count}")




