
def removeElement(nums, val: int) -> int:
    j = 0
    for num in nums :
        if num != val:
            nums[j] = num
            print(nums)
        
    return j
