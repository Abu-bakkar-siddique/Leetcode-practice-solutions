def sortPeople(names: str, heights: int) -> str:
    people_heights = list(tuple())
    for i in range(len(names)):
        people_heights.append((names[i], heights[i]))

    people_heights.sort(key= lambda item : item[1], reverse= True)
    return [t[0] for t in people_heights]

print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170])) 