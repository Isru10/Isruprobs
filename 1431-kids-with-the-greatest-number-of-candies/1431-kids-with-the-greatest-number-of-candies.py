class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        for i in range(len (candies)):
            if (candies [i]+extraCandies)>=max(candies):
                result.append(True)
                i+=1
            else:
                result.append(False)
                i+=1
        return result
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        