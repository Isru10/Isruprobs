class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1=len(s1)
        wc=Counter()
        
        for i, c in enumerate(s2):
            wc[c]+=1
            if i>=ls1:
                el=s2[i-ls1]
                if wc[el]==1:
                    del wc[el]
                else:
                    wc[el]-=1
            if wc==Counter(s1):
                return True 
        return False 
            
            
        
        
        
   