 # details explanation with animation : https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/1701107/Java-oror-Binary-Search-Explained-oror-Animation-Added-%3A)


# without binary search and time complexity is 0(len(num3)loglen(num3))

nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

# num3 = nums1 + nums1

# num3.sort()
# n = len(num3)

# if n%2==0:
#     print((num3[n //2 - 1] + num3[n // 2]) / 2)
# else:
#     print(num3[n // 2])



# Using binary search the problem is solved 

# if nums1 is None and nums2 is None:
#             return 0
        
#         if nums1 is None:
#             n = len(nums2)
#             return nums2[(n - 1) // 2] * 0.5 + nums2[n // 2] * 0.5
        
#         if nums2 is None:
#             n = len(nums1)
#             return nums1[(n - 1) // 2] * 0.5 + nums1[n // 2] * 0.5
        
#         if len(nums1) > len(nums2):
#             return self.findMedianSortedArrays(nums2, nums1)
        
#         n, m = len(nums1), len(nums2)
#         left, right = 0, n
        
#         while left < right:
#             i = (left + right) // 2
#             j = (n + m) // 2 - i
            
#             if nums1[i] < nums2[j - 1]:
#                 left = i + 1
#             else:
#                 right = i
        
#         first = left
#         second = (n + m) // 2 - left
        
#         shorterLeft = float('-inf') if first == 0 else nums1[first - 1]
#         shorterRight = float('inf') if first == n else nums1[first]
        
#         longerLeft = float('-inf') if second == 0 else nums2[second - 1]
#         longerRight = float('inf') if second == m else nums2[second]
        
#         if (n + m) % 2 == 1:
#             return min(shorterRight, longerRight)
#         else:
#             return max(shorterLeft, longerLeft) * 0.5 + min(shorterRight, longerRight) * 0.5




