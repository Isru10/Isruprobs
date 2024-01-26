class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmx, curmin=1,1
        
        for i in nums :
            if i ==0:
                curmx, curmin=1,1
            else:
                temp=curmx*i 
                curmx=max(i*curmx, i*curmin, i )
                curmin=min(temp, i*curmin, i )
                res=max(res, curmx)
        return res