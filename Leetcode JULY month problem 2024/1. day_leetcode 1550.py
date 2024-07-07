class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        
        for i in range(0, len(arr)):
            if arr[i] % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
    
solution = Solution()
list1 = list(map(int, input().split()))

print(solution.threeConsecutiveOdds(list1))
