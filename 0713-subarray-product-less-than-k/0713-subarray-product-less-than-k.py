class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        cnt=0
        prd=1
        l=0
        r=0
        while r<len(nums) :
            prd*=nums[r]
            while prd>=k:
                prd//=nums[l]
                l+=1
            cnt+=1+(r-l)
            r+=1
        return cnt 