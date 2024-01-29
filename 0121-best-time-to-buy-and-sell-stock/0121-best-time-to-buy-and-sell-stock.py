class Solution:
    def maxProfit(self, p: List[int]) -> int:
      
    
        maxp=0
        l=0
        r=1
        while r<len(p):
            cp=p[r]-p[l]
            if p[l]>p[r]:
                l=r
            else:
                maxp=max(maxp, cp)   
            r+=1
        return maxp 