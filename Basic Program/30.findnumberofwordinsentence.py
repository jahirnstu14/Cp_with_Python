# using split() functions in python 
sentence = input("Enter the sentence : ")
words = sentence.split()
print(f"The number of word in sentence is {len(words)}")

# without using default or building function in python 

sentence1 = input("Enter the sentence : ")
count = 0

for word in sentence1:
    if word==' ':
        count+=1
count+=1


print(f"The number of word in sentence is {count} ")