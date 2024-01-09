class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        best=0
        for x in nums:
            for y in nums :
                if abs(x - y) <= min(x, y):
                    best=max(best, x^y)
        return best