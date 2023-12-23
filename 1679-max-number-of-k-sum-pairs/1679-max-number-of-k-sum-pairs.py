class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        op=0
        l=0
        r=len(nums)-1
        while l<r:
            if( nums[l]+nums[r]==k):
                l+=1
                r-=1
                op+=1
            elif(nums[l]+nums[r]<k):
                l+=1
            else:
                r-=1
        return op
                