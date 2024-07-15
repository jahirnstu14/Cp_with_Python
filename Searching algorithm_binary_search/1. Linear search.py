my_list = list(map(int,input().split()))
target_value = int(input())

for i in range(len(my_list)):
    if my_list[i] == target_value:
        result = i
        break
    else:
        result = -1
        



if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
