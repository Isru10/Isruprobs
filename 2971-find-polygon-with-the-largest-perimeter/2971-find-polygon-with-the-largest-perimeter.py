class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        s=sum(nums)
        for i in range(n-1,1,-1):
            s-=nums[i]
            if s>nums[i]:
                return s+nums[i]
        return -1