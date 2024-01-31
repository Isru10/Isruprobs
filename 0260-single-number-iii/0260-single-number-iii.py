class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        d=Counter(nums)
        l=[]
        for i in d:
            if d[i]!=2:
                l.append(i)
        return l
                