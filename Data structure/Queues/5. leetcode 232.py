# best dicussion about the problem : https://www.youtube.com/watch?v=0ZUM0yhBtPI

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1 

# Example usage:
if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())  # Output: 1
    print(q.pop())   # Output: 1
    print(q.empty()) # Output: False
    q.pop()
    print(q.empty()) # Output: True
