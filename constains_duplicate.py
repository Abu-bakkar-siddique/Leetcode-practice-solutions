from collections import defaultdict
def hasDuplicate(nums: list) -> bool:
    count = defaultdict(bool)

    for num in nums:
        if num not in count:
            count[num] = True
        
        elif count[num] == True:
            return True
    
    return False
print(hasDuplicate([1,1,2,4,5]))

