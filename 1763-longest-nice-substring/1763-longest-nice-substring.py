class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        seen=set(s)
        for i in range( len (s)):
            if s[i ].lower() in seen and s[i].upper() in seen :
                continue 
            l=self.longestNiceSubstring( s[:i])
            r=self.longestNiceSubstring(s[i+1:])
            return max(l, r, key=len)
        return s