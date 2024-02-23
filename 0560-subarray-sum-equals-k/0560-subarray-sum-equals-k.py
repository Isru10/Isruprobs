class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=0
        d={0:1}
        ans=0
        for n in nums:
            ps+=n
            if ps-k in d:
                ans=ans+d[ps-k]
            d[ps]=d.get(ps,0)+1
        return ans 
       