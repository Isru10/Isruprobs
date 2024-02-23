class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ps=0
        pd={0:-1}
        
        for i in range(len(nums)):
            ps+=nums[i]
            rem=ps%k 
            if pd.get(rem) is not None:
                geti=pd[rem]
                if i-geti>=2:
                    return True 
            else:
                pd[rem]=i
        return False
             