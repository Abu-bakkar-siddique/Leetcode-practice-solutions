from collections import deque # double sided queue
class Mystack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
    
    def pop(self) -> int:
        if not self.empty():  return self.stack.pop()
        raise IndexError("index out of range")
    
    def top(self) -> int:
        if not self.empty():  return self.stack[-1]
        raise IndexError("index out of range")
    
    def empty(self):
        return len(self.stack) == 0
    

obj = Mystack()
obj.push(1)
obj.push(3)
obj.push(6)
obj.push(3)
obj.push(3)
obj.push(3)

print(obj.stack)
param_2 = obj.pop()
param_2 = obj.pop()
param_2 = obj.pop()
param_2 = obj.pop()

print(obj.top())
# param_4 = obj.empty()

print(obj.stack)
print(obj.empty())



"""Stack Implementation using Lists, slower than deque"""

# class MyStack:
#     def __init__(self):
#         self.stack = []
        
#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         if not len(self.stack) > 0: return
#         element = self.stack.pop(-1) # remove the last element 
#         self.stack = self.stack[0:] # slice the list after removing 
#         return element 
    
#     def top(self) -> int:
#         if len(self.stack) > 0: return self.stack[-1]

#     def empty(self) -> bool:
#         if len(self.stack) == 0 : return True
#         return False
            
# Your MyStack object will be instantiated and called as such:
