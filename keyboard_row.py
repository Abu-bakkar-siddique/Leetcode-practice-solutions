from collections import defaultdict
def findWords(words : list):
    """
    :type words: List[str]
    :rtype: List[str]
    """

    r_1 = set("qwertyuiop")
    r_2 = set("asdfghjkl")
    r_3= set("zxcvbnm")

    
    result = []

    for word in words:
        row1 = False
        row2 = False
        row3 = False

        for char in word.lower():
            if (char in r_1 and char not in r_2 and char not in r_3):
                row1 = True

            if (char in r_2 and char not in r_1 and char not in r_3):
                row2 = True

            if (char in r_3 and char not in r_2 and char not in r_1):
                row3 = True

        if sum([row1, row2, row3]) == 1:
            result.append(word)

    return result
print(findWords(["asad","hello", "zxc"]))


        

