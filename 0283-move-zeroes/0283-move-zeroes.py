class Solution(object):
    def moveZeroes(self, nums):
        temp=0
        for i in range(len (nums)):
                   if nums[i]!=0:
                          nums[i],nums[temp]=nums[temp],nums[i]
                          temp+=1  
        return nums