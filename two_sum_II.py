def twoSum(numbers: int, target: int) -> list[int]:
    pointer_1 = 0
    pointer_2 = len(numbers) - 1
    count = 0
    
    while True:
        # this case is to avoid the index out of range in case there exists no solution
        if pointer_1 == pointer_2 :
            return None
        
        if numbers[pointer_1] + numbers[pointer_2] > target:
            pointer_2 -= 1
        
        elif numbers[pointer_1] + numbers[pointer_2] < target:
            pointer_1 += 1
        else:
            return [pointer_1 + 1, pointer_2 + 1]

              
"""Test Cases"""

print(twoSum( numbers = [2,7,11,15], target = 9))
print(twoSum( numbers = [2,3,4,6], target = 6))
print(twoSum(numbers = [-1,0], target = -1))
print(twoSum(numbers = [5, 25, 75], target = 100))
print(twoSum([1, 40, 50,60,90, 122, 140, 215, 300, 350, 1222], 255))