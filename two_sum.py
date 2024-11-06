def twoSum(nums: int, target: int) -> int:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [i, hash_map[nums[i]]]
            
            hash_map[target - nums[i]] = i

print(twoSum([2, 7, 11], 18))
       




