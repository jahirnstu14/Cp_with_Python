class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []
        

    def push(self, x: int) -> None:
        # Only push the old minimum value when the current minimum value changes after pushing the new value x
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
    

    def pop(self) -> None:
        # If pop operation could result in the changing of the current minimum value, pop twice and change the current minimum value to the last minimum value.
        if self.stack.pop() == self.min:
            self.min = self.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min
        

# Example usage
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(3)
    minStack.push(5)
    print(f"Min: {minStack.getMin()}")  # Min: 3
    minStack.push(2)
    minStack.push(1)
    print(f"Min: {minStack.getMin()}")  # Min: 1
    minStack.pop()
    print(f"Min: {minStack.getMin()}")  # Min: 2
    minStack.pop()
    print(f"Top: {minStack.top()}")     # Top: 5
    print(f"Min: {minStack.getMin()}")  # Min: 3
