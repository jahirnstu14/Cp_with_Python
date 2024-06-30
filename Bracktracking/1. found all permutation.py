def permutation(at, n, used, number):
    if at == n + 1:
        for i in range(1, n + 1):
            print(number[i], end=" ")
        print()
        return

    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            number[at] = i
            permutation(at + 1, n, used, number)
            used[i] = False

def main():
    n = int(input())  # You can change n to any value you want
    # n = len(nums)
    used = [False] * (n + 1)
    number = [0] * (n + 1)
    permutation(1, n, used, number)

if __name__ == "__main__":
    main()
    
# leetcode solution :

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         used = [False] * n
#         number = [0] * n
#         result = []

#         def permutation(at):
#             if at == n:
#                 result.append(number[:])
#                 return

#             for i in range(n):
#                 if not used[i]:
#                     used[i] = True
#                     number[at] = nums[i]
#                     permutation(at + 1)
#                     used[i] = False

#         permutation(0)
#         return result
