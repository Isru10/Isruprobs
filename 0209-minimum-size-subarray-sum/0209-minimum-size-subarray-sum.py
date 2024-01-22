class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target :
            return 0
        ws=0
        l=0
        ans=float('inf')
        for r , val in enumerate (nums):
            ws+=val
            while ws>=target:
                ws-=nums[l]
                ans=min(ans, r-l+1)
                l+=1
        return ans