class Solution:
    def isPalindrome(self, s: str) -> bool:   
        l=[]
        for i in range(len(s)):
            if s[i].isalnum():
                l.append(s[i])
        p=(''.join(l)).lower()
        l=0
        r=len(p)-1
        while l<=r:
            if p[l]!=p[r]:
                return False 
            l+=1
            r-=1
        return True
    
    
    
    