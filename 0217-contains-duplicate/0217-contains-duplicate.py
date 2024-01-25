class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict=Counter (nums)
        for i in dict:
            if dict[i]>1:
                return True 
        return False
        