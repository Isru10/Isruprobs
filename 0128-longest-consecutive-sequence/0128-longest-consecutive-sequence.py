class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        res=1
        cnt=1
        nums=list(set(nums))
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i]-1==nums[i-1]:
                cnt+=1
                res=max(res,cnt )
            else:
                cnt=1
        return res
