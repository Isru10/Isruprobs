class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [i for i, j in Counter(nums).items() if j == 1]
