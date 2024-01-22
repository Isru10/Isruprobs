class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=sum(nums[:k])
        w=ans
        for i in range( len(nums)-k):
            w=w-nums[i]+nums[i+k]
            ans=max(ans, w)
        return ans/k

    
    

       
        
        