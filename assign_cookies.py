def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    s.sort()
    g.sort()

    """
    sorted:
        g = [1,3,5]
        s = [1,3,4]

    using a single loop

    n for counter
    j to track the second arrays variable
    """
    n = 0
    j = 0

    for i in range(len(s)):
        if s[i] >= g[i]:
            n += 1
            j += 1
        
        if j == len(g):
            break
    return n
g = [1,3,5]
s = [1,3,4]
print(findContentChildren(g, s))