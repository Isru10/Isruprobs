class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack :
            return -1
        else:
            k=len(needle)
            w=haystack[:k]
            for i in range(len(haystack)-k+1 ):
                w=haystack[i:k+i]
                if w==needle:
                    return i
                i+=1
        
        
        
        
        
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        