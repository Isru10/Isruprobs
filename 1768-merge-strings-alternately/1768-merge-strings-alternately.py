class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        ans=''
        rem=''
        if len(w1)>len(w2):
            rem=w1[len(w2):]
        if len(w2)>len(w1):
            rem=w2[len(w1):]
        for i in range(min(len(w1), len(w2))):
            ans+=w1[i]
            ans+=w2[i]
        ans+=rem
        return ans
        
            
        
     