class CustomStack: 
    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stack = [] 
        self.increment_tracking = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max:
            self.stack.append(x)
            self.increment_tracking.append(0)

    def pop(self) -> int:

        if not self.stack: return -1
        val = self.stack.pop() + self.increment_tracking[-1]

        if len(self.increment_tracking) > 1 :
            self.increment_tracking[-2] += self.increment_tracking[-1]
            self.increment_tracking.pop()
        else:
            self.increment_tracking.pop()

        return val
    
    def increment(self, k: int, val: int) -> None:
        # print(len(self.stack)) 
        # print("length of min tracking :", len(self.increment_tracking()))
        if k <= len(self.stack):
            self.increment_tracking[k - 1] += val
        else:
            if len(self.stack) != 0: self.increment_tracking[-1] += val

# class CustomStack:

#     def __init__(self, maxSize: int):
#         self.max = maxSize
#         self.element_count = 0
#         self.stack = []

#     def push(self, x: int) -> None:
#         if  self.element_count < self.max:   
#             self.stack.append(x)
#             self.element_count += 1

#     def pop(self) -> int:
#         if not self.stack: return -1
#         self.element_count -= 1 
#         return self.stack.pop()
        
#     def increment(self, k: int, val: int) -> None:
#          if k <= self.element_count:
#             for i in range(k):
#                self.stack[i] = self.stack[i] + val
         
#          else:
#             for j in range(self.element_count):
#                self.stack[j] += val
                
obj = CustomStack(maxSize = 4)
obj.push(2)
obj.push(23)
obj.push(12)

obj.increment(2,10)
print(obj.stack)

