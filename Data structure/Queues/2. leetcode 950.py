# linked for solution : https://leetcode.com/problems/reveal-cards-in-increasing-order/discuss/5001469/Faster-LesserDetailed-ExplainationSortingDequeStep-by-Step-ExplainationPythonJavaC%2B

from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        q = deque(range(n))
        ans = [0] * n
        
        for i in range(n):
            ans[q.popleft()] = deck[i]
            if q:
                q.append(q.popleft())
        
        return ans

# Example usage
solution = Solution()
deck = [17, 13, 11, 2, 3, 5, 7]
result = solution.deckRevealedIncreasing(deck)
print("Original deck:", deck)
print("Deck revealed in increasing order:", result)
