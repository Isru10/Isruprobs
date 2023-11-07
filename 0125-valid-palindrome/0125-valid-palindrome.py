class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        for i in s:
             if (False==i.isalnum()):
                s=s.replace(i,'')
        if(s==s[::-1]):
            return True
        return False