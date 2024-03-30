class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ln=0
        lf=0
        res=0
        cnt=defaultdict(int)
        
        for r in range(len (nums)):
            cnt[nums[r]]+=1
            while len(cnt)>k:
                cnt[nums[ln]]-=1
                if   cnt[nums[ln]]==0:
                     cnt.pop(nums[ln])
                
                ln+=1
                lf=ln
            while cnt[nums[ln]]>1:
                cnt[nums[ln]]-=1
                ln+=1
                
                
            if  len(cnt)==k:
                    res+=ln-lf+1
        return res 
            