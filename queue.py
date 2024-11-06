from collections import deque
class MyQueue:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if not self.empty() : return self.q.popleft()
        raise IndexError("queue is empty")
     
    def peek(self) -> int:
        if not self.empty() : return self.q[0]
        raise IndexError("queue is empty")

    def empty(self) -> bool:
        return len(self.q) == 0
    


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
obj.push(3)
obj.push(5)
obj.push(6)
obj.push(1)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(obj.q)