
# using kadadine algorithm which is used for subarray problem 

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i + 1
                gas_tank = 0
             
        return start_index

# Example usage:
sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # Output should be 3
print(sol.canCompleteCircuit([2,3,4], [3,4,3])) # Output should be -1