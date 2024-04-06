class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        for i in nums1:
            for j in range(nums2.index(i)+1, len(nums2)):
                if nums2[j]>i:
                    stack.append(nums2[j])
                    break
            else:
                stack.append(-1)
        return stack 