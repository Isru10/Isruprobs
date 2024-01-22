class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best=0
        zeros=0
        r=0
        l=0
        n=len(nums)
        while r<n:
            if nums[r]==0:
                zeros+=1
            while zeros>1:
                if nums[l]==0:
                    zeros-=1
                l+=1
            r+=1
            best = max(best , r-l-1)
        return best