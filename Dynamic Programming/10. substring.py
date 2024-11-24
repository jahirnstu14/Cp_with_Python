# A substring is a contiguous sequence of characters within a string. To count all non-empty substrings, we consider the starting and ending positions of the substring.
from itertools import count

# Count of non-empty substrings is count = n*(n+1)/2

# non empty substring find the number of substring with duplicate substring

for each_test in range(int(input())):
    string = input()
    result = []
    count = 0
    for i in range(len(string)):
        for j in range(i,len(string)):
            result.append(string[i:j+1])
            count +=1
    print(f"Number of substring {count} and The substrings are of string {string} is {result}")

# empty substring find the number of substring with duplicate substring

# for each_test in range(int(input())):
#     string = input()
#     result = [" "]
#     count = 0
#     for i in range(len(string)):
#         for j in range(i,len(string)):
#             result.append(string[i:j+1])
#             count +=1
#     print(f"Number of substring {count+1} and The substrings are of string {string} is {result}")


# distinct substring non empty using set

for each_test in range(int(input())):
    string = input()
    result = set()
    count = 0
    for i in range(len(string)):
        for j in range(i,len(string)):
            result.add(string[i:j+1])
    print(f"Number of substring {len(result)} and The substrings are of string {string} is {result}")

# with empty only add 1 with len(result)+1 , adding empty set = " "