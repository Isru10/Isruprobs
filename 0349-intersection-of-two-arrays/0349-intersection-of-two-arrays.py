class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numset=set()
        for i in nums1:
            if i in nums2:
                numset.add(i)
            i+=1
        return list(numset) if len(numset)>=1 else None