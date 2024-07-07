# implement stack using queue 

# best explanation for stack implementation using two queue and one queue : https://www.youtube.com/watch?v=Eh2gTUHL8Hs  and when lot of push operation needed that time i'll use two queue otherwise use one queue .

# important note : 
# Two-Queue Approach
# How it Works: Utilize two queues and move elements between them to mimic stack operations.
# Time Complexity: $$O(n)$$ for pop and top, $$O(1)$$ for push and empty.
# When to Use: Choose this approach when the frequency of push and empty operations is higher than pop and top.

# One-Queue Approach
# How it Works: Use a single queue and reorganize (rotate) its elements when pushing a new element.
# Time Complexity: $$O(n)$$ for push, $$O(1)$$ for pop, top, and empty.
# When to Use: Choose this approach when you expect pop and top operations to be more frequent than push.

# 4. Thought Process
# The two-queue approach is more straightforward but involves more element transfers for pop and top.
# The one-queue approach requires more work during the push operation but makes pop and top more efficient.

# solution using one queue

from collections import deque

class MyStack:

    def __init__(self):
        self.que = deque()

    # Push element x onto stack.
    def push(self, x):
        self.que.append(x)
        for _ in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

    # Removes the element on top of the stack and returns that element.
    def pop(self):
        if not self.empty():
            return self.que.popleft()
        return None

    # Get the top element.
    def top(self):
        if not self.empty():
            return self.que[0]
        return None

    # Return whether the stack is empty.
    def empty(self):
        return len(self.que) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# using two queue 

from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        poped_element  = self.q1.popleft()
        
        self.q1, self.q2 = self.q2, self.q1
        
        return poped_element

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top_element = self.q1[0]
        
        self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return top_element

    def empty(self) -> bool:
        return len(self.q1) == 0

# Code for testing the MyStack class
if __name__ == "__main__":
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print("Top element is:", obj.top())  # should return 2
    print("Popped element is:", obj.pop())  # should return 2
    print("Stack is empty:", obj.empty())  # should return False
    print("Popped element is:", obj.pop())  # should return 1
    print("Stack is empty:", obj.empty())  # should return True

