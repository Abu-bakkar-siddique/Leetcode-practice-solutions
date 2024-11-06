import string
from collections import defaultdict
def mostCommonWord(paragraph: str, banned) -> str:
    
    # removing the punctuatiions 
    hash_map = defaultdict(int)
    
    paragraph = paragraph.lower()
    for i in string.punctuation:
        paragraph = paragraph.replace(i, " ")

    paragraph = paragraph.strip().split(" ")
   
    for word in paragraph:
        if word != "" and not word.isspace() and word not in banned:
            hash_map[word] += 1
    
    max_occurrence = -1
    res = str()


    for key, value in hash_map.items():
        if value > max_occurrence:
            max_occurrence = value
            res = key
    return res
print(mostCommonWord("Bob. hIt, baLl",["bob", "hit"]))
