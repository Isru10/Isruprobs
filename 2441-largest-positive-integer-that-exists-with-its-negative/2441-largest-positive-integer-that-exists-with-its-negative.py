class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        r=len(nums)-1
        while r>=0 and nums[r]>0:
            l=0
            while nums[l]<0:
                if abs(nums[l])==nums[r]:
                    return nums[r] 
                
               
                l+=1
            r-=1
        return -1