class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if n<3:return 
        nums.sort()
        res=[]
        for p1 in range(n-2):
            if p1==0 or nums[p1]!=nums[p1-1]:
                p2, p3=p1+1, n-1
            while p2<p3:
                sum=nums[p1]+nums[p2]+nums[p3]
                if sum==0:
                    res.append([nums[p1], nums[p2], nums[p3]])
                    while p2 < p3 and nums[p2]==nums[p2+1]: p2+=1
                    while p2 <p3 and nums[p3]==nums[p3-1]:p3-=1
                    p2, p3 = p2+1, p3-1
                elif sum<0:p2+=1
                else : p3 -=1
        return res 