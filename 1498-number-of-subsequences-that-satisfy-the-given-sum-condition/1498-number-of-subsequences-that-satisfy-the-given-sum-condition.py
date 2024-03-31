class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod=10**9+7
        nums.sort()
        res=0
        r=len(nums)-1
        for i, left in enumerate(nums):
            while nums[r]+left>target and i <= r:
                r-=1
            if i<=r:
                res+=(2**(r-i))
                res=res%mod
        return res
        