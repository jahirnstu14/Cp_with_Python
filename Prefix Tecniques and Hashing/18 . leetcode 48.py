# hashmap problem solving 
from typing import List

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = defaultdict(list)  # here list inside the defaultdict means that it takes list in the values .
        # hashmap = {}  for empty dictionary 
        
        for s in strs:
            sort_string = tuple(sorted(s))  # whnen we use hashmap or dictionary 
            # if sort_string not in hashmap:
            #     hashmap[sort_string] = [] # for empty dictionary in comment execution 
                
            hashmap[sort_string].append(s)
        
        for group in hashmap.values():
            ans.append(group)
        return ans 
        

# Example usage:
solution = Solution()
print(solution.groupAnagrams(list(map(str,input().split()))))