class Solution(object):
    def strStr(self, haystack, needle):
        n2=len(needle)
        for i in range(len(haystack)):
            if(haystack[i:i+n2].__eq__(needle)):
                return i
        return -1