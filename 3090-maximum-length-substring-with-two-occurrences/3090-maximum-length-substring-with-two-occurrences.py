class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        mxl=0
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
            while d[s[i]]>2 and l<=i :
                d[s[l]]-=1
                l+=1
            mxl=max(mxl,i-l+1)
        return mxl