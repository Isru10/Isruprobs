class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans =sum(nums[:k])
        window=ans
        n=len(nums)
        for i in range(n-k):
            window=window-nums[i]+nums[i+k]
            ans=max(window,ans)
        return ans/k
        
        