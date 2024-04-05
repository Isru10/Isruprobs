from sortedcontainers import *
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sl=SortedList([nums[0]])
        l=0
        res=0
        for r in range(1,len(nums)):
            while sl and (nums[r]<sl[-1]-2 or sl[0]+2 <nums[r]):
                sl.remove(nums[l])
                l+=1
            sl.add(nums[r])
            res+=r-l+1
        return res+1