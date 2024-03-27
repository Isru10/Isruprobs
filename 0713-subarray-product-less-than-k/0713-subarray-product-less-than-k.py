class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        cnt=0
        prd=1
        l=0
        
        for r in range(len(nums)):
            prd*=nums[r]
            while prd>=k:
                prd=prd//nums[l]
                l+=1
            cnt+=(r-l+1)
        return cnt