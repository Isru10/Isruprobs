class Solution(object):
    def searchInsert(self, nums, target):
        i=0
        while(i<len(nums)):
            if(nums[i]>target or target==nums[i]):
                return i
            i+=1
        return i