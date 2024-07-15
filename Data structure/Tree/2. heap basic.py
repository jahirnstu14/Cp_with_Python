# this is the most underated video to learn heap clearly and i always will see this video at the time of learning heap and link is : https://www.youtube.com/watch?v=HqPJF2L5h9U

# Nicely discribe to problme identification of heap : https://www.youtube.com/watch?v=hW8PrQrvMNc&list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9

# In heap, each node has a number that is higher than all of its descendants , which means the higest value will be at the top .

# in heap, insertion will be from bottom to up  and deletion will be from root to down
# in heap, for creation heap by insertin node take nlog(n) and deletion full node from heap takes nlog(n)  and for maxheap after deletion node gives the asceding order. so, heapsort takes 0(n* logn)  times complexity .

# in heap, heapify means organized existing tree in a such way that it follows the heap minheap or max heap characteristics because, if we create heap by insertion node one by one then , time complexity will be nlog(n)  but if we use heapify method time complexity will be 0(n) because , only swapping occurs in among the n node in a tree

# the key charecteristics of headp :  it is a complete tree. if node  number is n . then height of a complete tree will be log(n) . 

# the different between binary tree and heap is that it can have duplicate value which is different from the binary tree

# there are two types of head. Max headp and min head.
# maxheap: where tree has the highest value at the top containing node in tree.
# minheap: where tree has the highest value at the top among the containing node in tree.

#                  99
#                 / \
#                72   61               
#               / \    / \
#              58  55 27  18

# value = * 99 72 61 58 55 27 18
# index = 0  1  2  3  4 5   6  7

# form list we can find left child and right child of parent :
    
# left_child = 2 * parent_index
# right_child = 2 * parent_index + 1

# example : parent = 99, which index = 1, so ,
# left_child index = 2 * 1 = 2 (from list index)= 72
# left_child index = 2 * 1 + 1 = 3(from listindex) = 72

# to find the parent of particular node:

# findex of parent node of that node =  ofinding node value//2 

# example : node 27 and 18 index is 6 and 7 . so, parent are 6/2 = 3 , 7/2=3.5 = 3 so, parent index 3 which denotes 61 .


# why heap is used :

# priority queue : if you said that the highest value was the higest priority and you want it to always remove the highest value from the queue , then heap is a really great way of doing this because, we always have the highest value at the top . 
# same thing is possible binary search tree but tree is not always balance in binary tree. for that time complexity will be 0(n) for worst case. 

# In heap, items remove from top and items add from bottom right side. it is the most important . the binary balance tree height is log(n) . In heap it is possible only 0(log(n))

# In priority queue , insertion and deletion are happeded according to the priority of elements  of queue. 
# if the list or  is =  4 5 6 7 1 2 3 and priority queue of the list is smallest number . in that time , don't maintain the queue condition of queue . deletion occur according to the priority. from above queue first will be delete smallest number 1, then 2 sequencially. if we use list complexity for deletion or inserion will be 0(n) . but if do implement it by minheap , it takes only log(n) times.

# if the list or  is =  4 5 6 7 1 2 3 and priority queue of the list is largest number . in that time , don't maintain the queue condition of queue . deletion occur according to the priority. from above queue first will be delete smallest number 7 then 6 sequencially.if we use list complexity for deletion or inserion will be 0(n) . but if do implement it by maxheap , it takes only log(n) times.



















