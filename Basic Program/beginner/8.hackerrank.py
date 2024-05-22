n = int(input())

length = 2 * n - 1
for i in range(length):
    for j in range(length):
        minimum = min(i, j, length - i - 1, length - j - 1)
        print(n - minimum, end=" ")
    print()
 
 
#  for input 7 output will be :
     
# 7 7 7 7 7 7 7 7 7 7 7 7 7 
# 7 6 6 6 6 6 6 6 6 6 6 6 7 
# 7 6 5 5 5 5 5 5 5 5 5 6 7 
# 7 6 5 4 4 4 4 4 4 4 5 6 7 
# 7 6 5 4 3 3 3 3 3 4 5 6 7 
# 7 6 5 4 3 2 2 2 3 4 5 6 7 
# 7 6 5 4 3 2 1 2 3 4 5 6 7 
# 7 6 5 4 3 2 2 2 3 4 5 6 7 
# 7 6 5 4 3 3 3 3 3 4 5 6 7 
# 7 6 5 4 4 4 4 4 4 4 5 6 7 
# 7 6 5 5 5 5 5 5 5 5 5 6 7 
# 7 6 6 6 6 6 6 6 6 6 6 6 7 
# 7 7 7 7 7 7 7 7 7 7 7 7 7 

