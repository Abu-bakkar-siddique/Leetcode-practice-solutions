import copy
def heightChecker(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        counter = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                counter += 1

        return counter    

print(heightChecker([1,3,4,5,8,1]))