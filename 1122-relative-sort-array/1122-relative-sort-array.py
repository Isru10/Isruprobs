class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a2s=set(arr2)
        nums1=[]
        nums2=[]
        for i in arr1:
            if i in arr2:
                nums1.append(i)
            else:
                nums2.append(i)
        hn1=Counter(nums1)
        ans=[]
        for i in arr2:
            ans+=[i]*hn1[i]
        return ans+sorted(nums2)
        