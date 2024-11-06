class MinStack:

   def __init__(self):
      self.stack = []
      self.min_tracking = []

   def push(self, val: int) -> None:

      if self.stack:
         if val <= self.min_tracking[-1]:
            self.min_tracking.append(val)

         elif val > self.min_tracking[-1]:
            self.min_tracking.append(self.min_tracking[-1])
         self.stack.append(val)
      else:
         self.stack.append(val)
         self.min_tracking.append(val)

   def pop(self) -> None:
      self.stack.pop()
      self.min_tracking.pop()

   def top(self) :
      return self.stack[-1]

   def getMin(self) :
      return self.min_tracking[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-90)
obj.push(-90)
obj.push(-440)
obj.push(-200)
obj.push(-350)
obj.push(-450)
obj.push(-290)

obj.pop()
obj.pop()

print(obj.stack)
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)
print(param_3)