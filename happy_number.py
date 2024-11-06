import math
from collections import defaultdict
def isHappy(n: int) -> bool:

    def compute(number : list) -> int :
        res = int()
        for digit in number:
            res += int(digit) * int(digit)    
        return res

    computed_sums = defaultdict(lambda: False)
    number_list = list(str(n))

    while(True):
        res = compute(number_list)
        if res == 1:
            return True
        
        elif computed_sums[res] == False:
            computed_sums[res] = True
            number_list = list(str(res))

        #cycle detected, means we are back at som value that was previously computed 
        elif computed_sums[res]:
            return False
        
print(isHappy(2))
