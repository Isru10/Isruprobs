class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l=0
        minl=float("inf")
        cur=0
        for r in range(len(nums)):
            cur|=nums[r]
            while cur>=k and l<=r:
                    minl=min(minl,r-l+1)
                    l+=1
                    cur=0
                    for i in range(l,r+1):
                        cur|=nums[i]
                        
        return minl if minl!=float("inf") else -1