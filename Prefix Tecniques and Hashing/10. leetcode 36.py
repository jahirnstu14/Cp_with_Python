# https://chatgpt.com/c/078fd602-7024-40dc-a330-e58d427da937  for remember multiple list, 2d, 3d in real life analogy

# len(board) = number of row  and len(board[0]) = number of column

from collections import defaultdict # 

def isValidSudoku():
    board = []
    for i in range(9):
        insert = list(map(str, input().split())) #for taking list of list or 2d list 
        board.append(insert)

    row = [defaultdict(int) for _ in range(9)]
    col = [defaultdict(int) for _ in range(9)]
    box = [defaultdict(int) for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = board[i][j]
                
                # if num in row[i]:
#                   row[i][num] += 1   it is the alternative of row[i][num] += 1
#               else:
#                   row[i][num] = 1
                
                
                # Check row
                row[i][num] += 1
                if row[i][num] > 1:
                    return False
                
                # Check column
                col[j][num] += 1
                if col[j][num] > 1:
                    return False
                
                # Check box
                k = (i // 3) * 3 + (j // 3)
                box[k][num] += 1
                if box[k][num] > 1:
                    return False

    return True

# Example usage
if __name__ == "__main__":
    result = isValidSudoku()
    if result:
        print("True")
    else:
        print("False")
               
# Wow this is an amazing solution.
# k = i // 3 * 3 + j // 3 wow!
# for those who need to visualize k > here

# 0  0  0 | 1  1  1 | 2  2  2
# 0  0  0 | 1  1  1 | 2  2  2
# 0  0  0 | 1  1  1 | 2  2  2
# --------+---------+---------
# 3  3  3 | 4  4  4 | 5  5  5
# 3  3  3 | 4  4  4 | 5  5  5
# 3  3  3 | 4  4  4 | 5  5  5
# --------+----------+--------
# 6  6  6 | 7  7  7 | 8  8  8
# 6  6  6 | 7  7  7 | 8  8  8
# 6  6  6 | 7  7  7 | 8  8  8
        
# row[i][board[i][j]]+=1 and why it is not acceptable in python ??   answer :
# In Python, directly incrementing a dictionary key's value with row[i][board[i][j]] += 1 is not acceptable if the key doesn't already exist in the dictionary. This is because Python dictionaries do not automatically handle missing keys. Attempting to access a key that doesn't exist will raise a KeyError.

# To avoid this, you need to check if the key exists in the dictionary first. If it doesn't, you should initialize it. This can be done in two ways:

# Using if-else to check and initialize the key:
# Using the collections.defaultdict which handles missing keys automatically.

# using if else:
# # Check row
# if num in row[i]:
#     row[i][num] += 1
# else:
#     row[i][num] = 1
# if row[i][num] > 1:
#     return False      