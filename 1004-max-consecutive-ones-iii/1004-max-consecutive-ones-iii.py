class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        for i in range(len(nums)):
            if nums[i]==0:
                k-=1
            if k<0:
                if nums[start]==0:
                    k+=1
                start+=1
        return i-start+1