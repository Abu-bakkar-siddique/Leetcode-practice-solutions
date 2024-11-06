from collections import defaultdict

def uniqueMorseRepresentations(words) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_codes = set()
        for word in words :
            morsed = str()
      
            for char in word:
                morsed += codes[ord(char) - 97]
            morse_codes.add(morsed)

        return len(morse_codes)

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))











# def uniqueMorseRepresentations(words: str) -> int:
#       codes = {
#     'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 
#     'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
#     'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
#     'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
#     'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
# }

#       count = 0
#       detection_map = defaultdict(bool) # to check duplicates
#       for word in words:
#             morse_code = str()
#             word = word.lower()
#             for char in word:
#                   morse_code += codes[char]
            
#             if not detection_map[morse_code]:
#                   detection_map[morse_code] = True
#                   count += 1
#       return count        
            
# print(uniqueMorseRepresentations(["Gin","zen","gig","msg"]))
# print(uniqueMorseRepresentations(["a"]))