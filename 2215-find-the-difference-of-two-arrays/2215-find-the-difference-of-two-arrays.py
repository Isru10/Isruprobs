class Solution(object):
    def findDifference(self, nums1, nums2):
        x=[]
        y=[]
        for i in range(len(nums1)):
            if (nums1[i] not in nums2) and (nums1[i] not in x):
                x.append(nums1[i])
        for j in range(len(nums2)):
            if (nums2[j] not in nums1) and (nums2[j] not in y):
                y.append(nums2[j])
        answer=[x,y]
        return answer
        
        
        
        
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        