class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        vals=list(count.values())
        mx=max(vals)
        ct=vals.count(mx)
        return ct*mx
        