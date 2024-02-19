class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float("inf")
        l=0
        ws=0
        if sum(nums)<target:return 0
        for r in range(len(nums)):
            ws+=nums[r]
            while target<=ws:
                res=min(res, r-l+1)
                ws-=nums[l]
                l+=1
        return res
      
        
       