n = int(input())
mylist = list(map(int,input().split()))

for i in range(1,n):
    tem = mylist[i]
    j = i-1
    while tem<mylist[j] and j>-1:
        mylist[j+1] = mylist[j]
        mylist[j] = tem
        j-=1
print(f"the sorted list is {mylist}")

# the worst complexity is 0(n^2) . and best time complexity = 0(n) because , for sorted or almost  array while loop will not executed 

# note:

# first we consider . two part sorted array and unsorted array , example : 5 4 1 2 3 
# here, 5 is sortedlist and 4 1 2 3 . then we insert into 4 to sorted arrary. then sorted will be 5,4 and unsorted array 1,2,3
# if 5 is greater than 4 . so , the array is not sorted for soring i will do swap 4 and 5 then , sorted list will be 4,5 and unsorted array 1,2,3.
# after that add in last 1 to sorted list. so, sorted list is not sorted . for 5 and 1 are not sorted. for this we will swap 5 and 1 .after that the sorted array is not sorted then , we will do swap 4 and 1 then the sorted array will be sorted.

