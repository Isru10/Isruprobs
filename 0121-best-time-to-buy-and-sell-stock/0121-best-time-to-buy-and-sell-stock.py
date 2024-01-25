class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l=0
        r=1
        mxp=0
        while r<len(p): 
            if p[l]<p[r]:
                c=p[r]-p[l]

                mxp=max(c, mxp)
            else:
                l=r
            r+=1
        return mxp
       