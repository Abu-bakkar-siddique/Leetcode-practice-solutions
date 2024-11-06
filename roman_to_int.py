def romanToInt(s):
    """
    :type s: str
    :rtype: int
    create a hash table for mapping roman to integers 
    """

    map_values = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,'C' : 100, 'D' : 500 , 'M' : 1000 }
    num = 0
    i = 0
    while(i < len(s)) :
            
            if i != len(s) - 1 and (map_values[s[i]]  < map_values[s[i + 1]]) :
                num += (map_values[s[i + 1]] - map_values[s[i]])
                i += 2

            else:  
                if i < len(s) :
                    num += map_values[s[i]] 
                    i += 1
    return num
print(romanToInt("IXX"))