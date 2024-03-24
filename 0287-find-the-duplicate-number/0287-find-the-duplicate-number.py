class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set()
        s.add(nums[0])
        for i in nums[1:len(nums)+1]:
            if i in s :
                return i 
                break 
            else:
                s.add(i)