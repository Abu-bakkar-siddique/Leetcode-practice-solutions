import copy
def oddString(words):
        first_array = []
        count = 0
        second_array = []

        for j in range(len(words)):
            difference_arary = []
            for i in range(1, len(words[j])):
                difference_arary.append(ord(words[j][i]) - ord(words[j][i - 1]))

            if j == 0:
                first_array = difference_arary

            if first_array != difference_arary: 
                next_diff = []
                if j != len(words) - 1:
                    for k in range(1, len(words[j+1])):
                        next_diff.append(ord(words[j + 1][k]) - ord(words[j + 1][k - 1]))
                    if next_diff == difference_arary and (first_array != next_diff):
                        return words[0]
                return words[j]

words = ["ddd","poo","baa","onn"]
print(oddString(words))


            
            
            
