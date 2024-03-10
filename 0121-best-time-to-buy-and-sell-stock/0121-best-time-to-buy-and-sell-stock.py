class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res=0
        l=0
        for r in range(len(p)):
            if p[r]>p[l] :
                res=max(res, p[r]-p[l])
            else:
                l=r
        return res