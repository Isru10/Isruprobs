class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k= len(nums)
        for i in range(k):
            mini= i 
            for j in range(i,k):
                if nums[mini]>nums[j]:
                    mini=j
            nums[mini],nums[i]=nums[i], nums[mini]
                    
        return nums 