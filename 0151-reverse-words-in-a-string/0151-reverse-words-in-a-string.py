class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        return ' '.join(s[::-1])
        
        """
        :type s: str
        :rtype: str
        """
        