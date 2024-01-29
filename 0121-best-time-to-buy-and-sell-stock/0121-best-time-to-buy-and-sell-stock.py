class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l=0
        res=0
        for r in range(len(p)):
            if p[l]>p[r]:
                l=r
            else:
                res=max(res,p[r]-p[l])
        return res