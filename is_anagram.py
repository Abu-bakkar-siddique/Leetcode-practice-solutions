from collections import Counter
def removeAnagram( words: list) -> list:
    # two pointers 
    i = 1
    j = 0
    while(i < len(words)):
        if sorted(words[i]) == sorted(words[j]):
            del words[i]
        else:
            i += 1
            j += 1
    
    return words
print(removeAnagram(["z","z","z","gsw","wsg","gsw","krptu"]))