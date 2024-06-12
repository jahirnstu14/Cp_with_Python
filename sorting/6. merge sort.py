def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
            
    while i < len(array1):
        combined.append(array1[i])
        i += 1
        
    while j < len(array2):
        combined.append(array2[j])
        j += 1
        
    return combined

def mergesort(mylist):
    if len(mylist) <= 1:
        return mylist
    mid = len(mylist) // 2
    left = mergesort(mylist[:mid])
    right = mergesort(mylist[mid:])
    return merge(left, right)

original_list = list(map(int, input().split()))
sorted_list = mergesort(original_list)
print(sorted_list)
