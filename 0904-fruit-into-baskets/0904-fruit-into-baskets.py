class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        counter=defaultdict(int)
        res=0
        l=0
        for r in range(len(nums)):
            counter[nums[r]]+=1
            while len(counter)>2:
                counter[nums[l]]-=1
                if counter[nums[l]]<1:
                    counter.pop(nums[l])
                l+=1
            res=max(res,r-l+1)
        return res 
            
