
import math
def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
                s[i], s[~i] = s[~i], s[i]
        return s
print(reverseString(["h","e","l","l","o"]))
print((7//3) + 1)