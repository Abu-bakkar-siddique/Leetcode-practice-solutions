def isValid (s : str)-> str:
   stack = []
   hash_map = {']' : '[', ')':'(', '}': '{'} # only the closing paranthesis as keys 
   opening_set = "([{"

   for char in s:

      if char in hash_map:
            if not stack or stack[-1] != hash_map[char]:
               return False
            stack.pop()

      elif char in opening_set:
            stack.append(char)
            
   return len(stack) == 0

print(isValid(''))