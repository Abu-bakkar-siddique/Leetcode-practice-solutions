
def searchMatrix (matrix: list, target: int) -> bool:
    i = 0 # row
    j = 0 # col

    k = len(matrix) - 1 # row
    l = len(matrix[0]) - 1 # col

    mid_i = (i + k) // 2 # mid row
    mid_j = (j + l) // 2 # mid col

    while i <= k and j <= l :
        
        if matrix[mid_i][mid_j] == target:
            return True

        # move left
        elif  target < matrix[mid_i][mid_j]:
            if mid_j == 0 :
                k = mid_i - 1
                l = len(matrix[0]) - 1

            else:
                l = mid_j - 1

        # move right 
        else:
            if mid_j == len(matrix[0]) - 1:
                i = mid_i + 1
                j = 0

            else:
                j = mid_j + 1
        mid_i = (i + k) // 2 # mid row
        mid_j = (j + l) // 2 # mid col
    
    return False


        


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60],[61,64,66,78],[79,81,88,89],[91,94,98,99]],79))


# # print(searchMatrix([[1,2,3],[4,5,6], [7,8,9]],5))
# print(searchMatrix([[1,2,3,4,5]],5))
# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60],[61,64,66,78],[79,81,88,89],[91,94,98,99]],79))
# """
# [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]
# 5

# []
# 5

# [
#   [5]
# ]
# 5

# [
#   [1, 2, 3, 4, 5]
# ]
# 3

# [
#   [1],
#   [2],
#   [3],
#   [4],
#   [5]
# ]
# 4

#     [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
#     ]
#     5


# [
#   [7, 7, 7],
#   [7, 7, 7],
#   [7, 7, 7]
# ]
# 7

# ]"""