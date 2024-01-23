class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        a=Counter (nums1)
        b=Counter (nums2)
        for i in a :
            if b.get (i) is not None:
                l+=min(a[i], b[i])*[i]
        return l
   