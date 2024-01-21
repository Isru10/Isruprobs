class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p=0
        for i in t :
            if p==len(s ): return True 
            if s[p]==i : p+=1
        return len(s )==p