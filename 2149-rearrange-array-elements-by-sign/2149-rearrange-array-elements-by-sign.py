class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i  in nums :
            if i>=0:
                p.append(i)
            else:
                n.append(i)
        i1,i2=0,0
        ans=[]
        while i2<len(nums)//2:
            ans.append(p[i1])
            i1+=1
            ans.append(n[i2])
            i2+=1
        return ans 