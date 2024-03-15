class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        num=0
        cnt=0
        for i in range(len(nums)):
            num+=nums[i]
            if num == 0:
                cnt+=1
        return cnt
                