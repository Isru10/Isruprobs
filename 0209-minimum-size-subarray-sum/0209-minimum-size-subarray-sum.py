class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        ws=0
        l=0
        if sum(nums)<target: return 0
        for r in range( len ( nums)):
            ws+=nums[r]
            while target<=ws:
                ans=min(ans,r-l+1 )
                ws-=nums[l]
                l+=1
            r+=1
        return ans 
        
        
       