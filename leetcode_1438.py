

def longestSubarray(nums, limit):
    def check_difference( sub_array, limit):

        for i in range(len(sub_array)):
            for j in range( i + 1,len(sub_array)):
                if abs(sub_array[i] - sub_array[j]) > limit:
                    return False
        return True
 

    sub_array = None
    size = 0
    for i in range(len(nums)):
        for j in range(i,len(nums) + 1):
            if i == j:
                sub_array = [nums[i]]
                if 0 <= limit and len(sub_array) >= size:
                    size = len(sub_array)       
                continue
             
            else:
                sub_array = nums[i:j]
                if check_difference(sub_array, limit): 
                    if len(sub_array) > size:
                        size = len(sub_array)
  
    return size
integer_list = list(range(1, 2001))
print(longestSubarray(integer_list, 3))