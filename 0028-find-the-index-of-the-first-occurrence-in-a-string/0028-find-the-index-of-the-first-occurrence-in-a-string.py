class Solution(object):
    def strStr(self, haystack, needle):
       ni=len(needle)
       for i in range(len(haystack)):
            if (haystack[i:i+ni].__eq__(needle)):
                return i
       else: return -1