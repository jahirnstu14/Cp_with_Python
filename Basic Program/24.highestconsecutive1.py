arr_string = input("Enter string which consists only of 0s and 1s: ")
count = 0
maximum = 0
for i in range(len(arr_string)):  # Use range() to iterate over indices
    if arr_string[i] == '1':  # Access character at index i
        count += 1
        maximum = max(count, maximum)
    else:
        count = 0
print(f"maximum number of consecutive 1s is {maximum}")
