class Solution:
    def maxArea(self, h: List[int]) -> int:
        res=0
        l=0
        r=len(h)-1
        while l<r:
            area=min (h[l],h[r])*(r-l)
            res=max(res,area)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return res 