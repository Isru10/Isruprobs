class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d={}
        l=0
        cnt=0
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
            while  d[nums[i]]>k:
                d[nums[l]]-=1 
                l+=1  
                
            cnt=max(cnt,i-l+1)
        return cnt 