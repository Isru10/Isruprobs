class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        n=0
        for i in (nums):
            if c[i]!=2:
                n=i
        
      
            
            
            
        return n