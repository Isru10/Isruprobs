class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i=0
        count=0
        while i<len (nums):
            j=i
            while j<len (nums ):
                
                if nums[i]==nums[j] and i<j:
                    count+=1
                j+=1
            i+=1
        return count 