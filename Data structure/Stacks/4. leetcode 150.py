# to understand clearly the discussion the solution : https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/1229370/Short-and-Simple-Solution-w-Explanation-or-O(N)-and-O(1)-Space-Solutions

from typing import List
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in {"+","-","*","/"}:
                stack.append(int(i))
            else:
                b, a = stack.pop(), stack.pop()
                
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                else:
                    stack.append(trunc(a / b)) # or it can be written by  a // b
        return stack[0]

def run_tests():
    solution = Solution()
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
    ]
# In summary : Using enumerate(test_cases, 1) allows you to iterate over the test cases with a counter starting at 1. This makes it easier to reference and print the test case number in a human-friendly way. The for i, (tokens, expected) part unpacks each test case tuple into its components, making it easy to use them inside the loop.

    for i, (tokens, expected) in enumerate(test_cases, 1):
        result = solution.evalRPN(tokens)
        if result == expected:
            print(f"Test case {i} passed: got {result}, expected {expected}")
        else:
            print(f"Test case {i} failed: got {result}, expected {expected}")

if __name__ == "__main__":
    run_tests()
    
# it will be my original for giving submit problem 

