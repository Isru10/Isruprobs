class Solution:
    def maximumLength(self, s: str) -> int:
        win=0
        d={}
        l=0
        while win < len(s):
            if s[win] in d :
                d[s[win]]+=1
            else:
                d[s[win]]=1
            c=win +1
            while  c <len(s) and s[win]==s[c]:
                if s[win:c+1] in d :
                    d[s[win:c+1]]+=1
                else :
                    d[s[win:c+1]]=1
                c+=1
            win+=1
        ans =-1
        for k,v in d.items():
            if v >=3 :
                ans =max(ans,len(k))
        return ans