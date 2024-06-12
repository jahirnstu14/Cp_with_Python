# discussion about selection sort : https://baburjhuli.blogspot.com/2022/02/selection-sort-algorithm.html

# bubble sort last er element theke sort kara shuru kare kinto selection sort er khetre first theke sort kara shuru hay :

n = int(input())
mylist = list(map(int,input().split()))

for i in range(len(mylist)-1):
    min = i
    for j in range(i+1,len(mylist)):
        if mylist[j] < mylist[min]:
            min = j
    if i!=min:
        tem = mylist[i]
        mylist[i] = mylist[min]
        mylist[min] = tem
        
print(mylist)    