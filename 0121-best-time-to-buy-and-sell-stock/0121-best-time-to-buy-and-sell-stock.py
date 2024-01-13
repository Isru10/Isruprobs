class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l=0
        r=1
        mxp=0
        while r<len(p):
            cp=p[r]-p[l]
            if p[l]<p[r]:
                mxp=max(mxp, cp)
            else: 
                l=r
            r+=1
        return mxp