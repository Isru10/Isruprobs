class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s=set(nums1)
        for i in range(len(nums2)):
            if nums2[i] in s:
                return nums2[i]
        return -1
            
       