class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c={}
        arr=[]
        for i in nums:
            c[i]=c.get(i,0)+1
            if c[i] ==2:
                arr.append(i)
        return arr 
                
        
       
        
    