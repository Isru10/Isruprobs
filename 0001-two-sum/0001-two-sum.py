class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i, n in enumerate(nums):
            if n in dict :
                return [dict[n], i]

            dict[target - n ]= i
            