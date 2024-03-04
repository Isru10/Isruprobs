class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans=0
        ps=0
        d={0:1}
        for num in nums:
            ps+=num
            key=ps%k
            if key in d :
                ans=ans+d[key]
            d[key]=d.get(key,0)+1
        return ans 