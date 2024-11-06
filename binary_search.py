def search(nums: int, target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l<= r:
        middle = (l + r) // 2
        if nums[middle] == target:
            return middle

        elif target > nums[middle] :    
            l = middle + 1
        
        elif target < nums[middle]:
            r = middle - 1
        
    else:
        return -1

"""
[-1,0,43,54,66,67,100,454,5655,6434] 55


"""

print(search([0,2,3,4,6,7,8,12,34,56,78,234,5788], 55))



    
