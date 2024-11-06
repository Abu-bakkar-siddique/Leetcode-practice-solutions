def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    index_sum = float('inf')

    map_1 = dict()
    map_2= dict()
    for i in range(len(list1)):
        map_1[list1[i]] = i 

    for j in range(len(list2)):
        map_2[list2[j]] = j

    result = list()
    for i in range(len(list1)): 
        if list1[i] in list2:
            if (i + map_2[list1[i]] < index_sum):

                index_sum = i + map_2[list1[i]]
                result = []
                result.append(list1[i])

            elif i + map_2[list1[i]] == index_sum:
                result.append(list1[i])
    return result

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

print(findRestaurant(list1, list2))
