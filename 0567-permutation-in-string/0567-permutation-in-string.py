class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1=len(s1)
        s1c=Counter(s1)
        wc=Counter()
        for i , c in enumerate(s2):
            wc[c]+=1
            if i >=ls1:
                el=s2[i-ls1]
                if wc[el]==1:
                    del wc[el]
                else:
                    wc[el]-=1
            if wc==s1c:
                return True 
        return False 
    