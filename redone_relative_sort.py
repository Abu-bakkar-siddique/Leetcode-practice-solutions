from collections import Counter
def relative_sort(arr1 : list, arr2 : list):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    
    element_count = Counter(arr1)
    result = list()
    left = list()

    for num in arr2:
        if num in arr1: 
            # could have used a loop here 
            for j in range (element_count[num]):
                result.append(num)
        

    for k,v in element_count.items():
        if k not in arr2:
            left.append(k)
            
    return result + sorted(left)

print(relative_sort([1,4,5,2,5,6,7,6,4,5,7,6,5,3,2,3,5,6,7,88,6,5,4,3,3,3,2], [5,6,1]))


        
            