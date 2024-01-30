class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            if s==c:
                return i 
            s-=nums[i]
        return -1 