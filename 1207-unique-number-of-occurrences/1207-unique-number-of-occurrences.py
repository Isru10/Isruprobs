class Solution(object):
    def uniqueOccurrences(self, arr):
        return sum(set(Counter(arr).values()))== len(arr)
        
        
        
        
        
        """
        :type arr: List[int]
        :rtype: bool
        """
        