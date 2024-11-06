
def scoreOfString(s):
    """
    :type s: str
    :rtype: int

    algorithm
    loop through the string
        sub = subtract the ascii of next from the current
        sum += sub
        """
    sum = 0
    for i in range(0, len(s) - 1):
         sum= sum + abs(ord(s[i]) - ord(s[i+1]))
    return sum

# top leetcode answer
def score_of_string(s):
    # return sum((abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1) ))
 return sum( (abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) -1) ))
print(score_of_string("helloworld"))