
# https://leetcode.com/problems/word-pattern/discuss/2976894/Daily-LeetCoding-Challenge-January-Day-1

# four solution has been given in the below 

# Pythonic solution 

# pattern = input()
# s = input().split()
# if len(set(zip(pattern,s))) == len(set(pattern))==len(set(s)) and len(pattern)==len(s):
#     print("True")
# else:
#     print("False")

# Using dictinary and set 

# pattern = input()
# s = input().split()

# if len(pattern)!=len(s):
#     print("False")

# d = {}
# se = set()


# for i in range(len(pattern)):
#     if pattern[i] in d:
#         if d[pattern[i]]!=s[i]:
#             print("False")
    
#     else:
#         if s[i] not in se:
#             d[pattern[i]]=s[i]
#             se.add(s[i])
#         else:
#             print("False")
            
# print("True")

# the time complexity will be : for above program :
# Time complexity:
# $$O(n)$$

# As it iterates through the s string and for searching if a key is present in a dict, the value in the set is O(1), and each time for each element in the s string, it should iterate, which is O(n).

# Space complexity:
# $$O(n)$$

# As one set and dict and list are used, the maximum space will be O(3n), which is nothing but O(n).
            
# for checking zip function in python how works:https://chatgpt.com/c/48725a93-3407-4db7-8da6-c2d899625658     
 
#  using hashmap and dictionary efficient way /// it is most choiceable solution :

pattern = input()
s = input().split()

w_to_p= dict()
if len(s)!=len(pattern):
    print("False")
if len(set(s))!=len(set(pattern)):
    print("False")
    
for i in range(len(s)):
    if s[i] not in w_to_p:
        w_to_p[s[i]]=pattern[i]
    elif w_to_p[s[i]]!=pattern[i]:
        print("False")

print("True")


# Using only hashmap with zip functions :
    
pattern = input()
s = input().split()

if len(pattern)!= len(s):
    print("False")

Hashmap = {}

for char, word in zip(pattern,s):
    if char not in Hashmap:
        Hashmap[char] = word
    else:
        if Hashmap[char]!=word:
            print("False")
            
if len(set(Hashmap.values())) != len(Hashmap):
    print("False")
else:
    print("True")
        

        