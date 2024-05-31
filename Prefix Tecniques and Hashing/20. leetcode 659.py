# https://www.lintcode.com/problem/659/ google company 

# Here is the extracted text from the provided image:

# Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Please implement encode and decode.
# Example1
# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"



input_list  = list(map(str,input().split()))
res = ""

for stringadd in input_list:
    res+=str(len(stringadd)) + "#" + stringadd
    


result,i = [],0

while i<len(res):
    j=i
    while res[j]!="#":
        j+=1
    length = int(res[i:j]) # The expression length = int(s[i:j]) is used to extract a substring from the string s starting at index i and ending just before index j, and then convert that substring into an integer. 
    result.append(res[j+1:j+1+length])
    i = j+1+length
print(result)    