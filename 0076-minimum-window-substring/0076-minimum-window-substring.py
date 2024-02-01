class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=="": return ""
        window,tcount={},{}
        for i in t:
            tcount[i]=tcount.get(i,0)+1
        need,have =len(tcount), 0
        reslen,res=float("inf"),[-1,-1]
        l=0
        for r in range(len (s)):
            c=s[r]
            window[c]=window.get (c, 0)+1
            if c in tcount and window[c]==tcount[c]:
                have+=1
            while have==need:
                if (r-l+1 )< reslen:
                    reslen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in tcount and window[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1]