# without stack using normal concept 

class Solution:
    def isValid(self, s: str) -> bool:
        # The while loop will continue as long as there are characters in the string
        while len(s) > 0:
            length_before = len(s)
            s = s.replace('()','').replace('{}','').replace("[]",'') # time complexity for  replace function in python is 0(n) . so, total complexity will be 0(len(s) * n )
            
            if length_before == len(s):
                return False
        return True
            
# Example usage:
solution = Solution()
print(solution.isValid("(){}[]"))  # Output: True
print(solution.isValid("([{}])"))  # Output: True
print(solution.isValid("(]"))      # Output: False
print(solution.isValid("([)]"))    # Output: False

# brute force solution will be using two loop where time complexity would have been 0(n^2)

# now for 0(n) solution i'll use STACK data structure

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif not stack: #if stack is empty then, return false .easy way , not stack means stack.empty()...
                return False
            
            elif stack[-1] == '(' and char == ')': # stack[-1] represent the top element 
                stack.pop()
            elif stack[-1] == '{' and char == '}':
                stack.pop()
            elif stack[-1] == '[' and char == ']':
                stack.pop()
            else:
                return False
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("(){}[]"))  # Output: True
print(solution.isValid("([{}])"))  # Output: True
print(solution.isValid("(]"))      # Output: False
print(solution.isValid("([)]"))    # Output: False


# another way solution using dictionary and stack  for more optimal solution 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Create a mapping of opening to closing brackets
        mapping = {'(': ')', '[': ']', '{': '}'}
        
        # Iterate over each character in the input string
        for char in s:
            # If the character is an opening bracket
            if char in mapping: # if we consider key only from mapping or dictionary 
                # Push the corresponding closing bracket onto the stack
                stack.append(mapping[char])
            else:
                # If the stack is empty or the top of the stack is not the matching closing bracket
                if not stack or stack[-1] != char:
                    return False
                # Pop the top element from the stack
                stack.pop()
        
        # If the stack is empty, all opening brackets were matched; otherwise, it is not valid
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("(){}[]"))  # Output: True
print(solution.isValid("([{}])"))  # Output: True
print(solution.isValid("(]"))      # Output: False
print(solution.isValid("([)]"))    # Output: False






