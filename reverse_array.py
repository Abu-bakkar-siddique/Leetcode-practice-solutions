arr = [1,4,5,6,7,5,3,4,56,7,8,9,7,5]

first = 0
last = len(arr) - 1

while first < last:
    arr[first] , arr[last] = arr[last], arr[first]
    first += 1
    last -= 1

print (arr)