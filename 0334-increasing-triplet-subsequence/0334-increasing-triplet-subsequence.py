class Solution(object):
    def increasingTriplet(self, nums):
        f=s=float('inf')
        for i in nums:
            if i <= f:
                f=i
            elif i<=s:
                s=i
            else:
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        