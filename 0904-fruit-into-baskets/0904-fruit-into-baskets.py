class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        d=defaultdict(int)
        l=0
        res=0
        for r in range(len(nums)):
            d[nums[r]]+=1
            while len(d)>2:
                d[nums[l]]-=1
                if d[nums[l]]<1:
                    d.pop(nums[l])
                l+=1
            res=max(res,r-l+1)
        return res
      