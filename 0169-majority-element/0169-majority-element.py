class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        result=0
        carry=0
        for c in count:
            if count[c]>result: 
                result=max(result,count[c])
                carry=c
        return carry 