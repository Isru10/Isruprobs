class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        c1=Counter(nums1)
        c2=Counter(nums2)
        for i in c1:
            if i in c2:
                return i 
        return -1
    
   