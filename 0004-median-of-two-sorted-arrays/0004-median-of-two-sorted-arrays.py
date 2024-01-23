class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=[0]* (len(nums1)+ len(nums2))
        i1=0
        i2=0
        for i in range( len ( merged)):
            if i2<len(nums2) and (i1==len(nums1) or nums2[i2]<nums1[i1]):
                merged[i]= nums2[i2]
                i2+=1
            else:
                merged[i]= nums1[i1]
                i1+=1   
        
        if len(merged) % 2==1:
            return  merged[len(merged)//2]
        
        else: 
            return  (merged[len(merged)//2]  +   merged[len(merged)//2 -1]  )/2.0  
            
        