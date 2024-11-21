
# brute force method for solving and finding combination of 6c3 = 20
# def findTripletBruteForce(arr, N, P):
#     # Iterate over all triplets
#     for i in range(N-2):
#         for j in range(i+1,N-1):
#             for k in range(j+1,N):
#                 if arr[i]+arr[j]+arr[k] == P:
#                     return "it is true"
#
#
# # Input
# N = int(input("Enter the size of the array: "))
# if N < 3:
#     print("No triplet found")
# else:
#     arr = list(map(int, input("Enter the elements of the array: ").split()))
#     P = int(input("Enter the target value: "))
#
#     # Output
#     print(findTripletBruteForce(arr, N, P))


# now using two pointer same thing less time complexity
def findTriplet(arr, N, P):
    # Sort the array
    arr.sort()

    for i in range(N-2):
        j = i+1
        k = N-1

        while j < k :
            current_sum = arr[i] + arr[j] + arr[k]
            if current_sum == P:
                return f"{arr[i]} {arr[j]} {arr[k]}"
            elif current_sum < P:
                j+=1
            else:
                k-=1


# Input
N = int(input("Enter the size of the array: "))
if N < 3:
    print("No triplet found")
else:
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    P = int(input("Enter the target value: "))

    # Output
    print(findTriplet(arr, N, P))
