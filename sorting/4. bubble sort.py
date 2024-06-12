# https://baburjhuli.blogspot.com/2022/02/bubble-sort-algorithm.html

# O(n2 - n) কে আমরা O(n^2) লিখতে পারি কারণ n2 এর তুলনায় n ছোট  and space complexity is 0(1)

n = int(input())
mylist = list(map(int,input().split()))

for i in range(len(mylist)-1):
    for j in range(0,len(mylist)-i-1):
        if mylist[j]>mylist[j+1]:
            temp  = mylist[j]
            mylist[j] = mylist[j+1]
            mylist[j+1] = temp
            # in python for swapping we can write shortly : mylist[j] , mylist[j+1] = mylist[j+1] , mylist[j]
print(mylist)

