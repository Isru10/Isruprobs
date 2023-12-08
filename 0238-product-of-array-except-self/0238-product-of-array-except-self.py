class Solution(object):
    def productExceptSelf(self, nums):
        post_product=1
        pre_product=1
        n=len(nums)
        output=[0]*n
        for i in range(n):
            output[i]=pre_product
            pre_product*=nums[i]
        for i in range(n-1, -1,-1):
            output[i]*=post_product
            post_product*=nums[i]
        
        
        
        return output
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        