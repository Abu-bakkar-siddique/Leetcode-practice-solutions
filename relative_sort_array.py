from collections import defaultdict
def relativeSortArray(arr1, arr2):
    # better for looking /searching
    arr2  = set(arr2)
    count = defaultdict(int)
    sub_array = []
    result = []
    for _ in arr1:
        if _ in arr2:
            count[_] += 1
        else:
            sub_array.append(_)
    for n in arr2:
        for i in range(count[n]):
            result.append(n)
    return result + sub_array
print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))