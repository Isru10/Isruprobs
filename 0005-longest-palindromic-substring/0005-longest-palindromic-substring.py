class Solution:
    def longestPalindrome(self, s: str) -> str:
        def exec( l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1: r]
        longest=''
        for i in range(len(s)):
            od=exec(i, i)
            ev=exec(i, i+1)
            if len(od)>len(longest):
                longest =od
            if len(ev)>len(longest):
                longest =ev
        return longest 
            