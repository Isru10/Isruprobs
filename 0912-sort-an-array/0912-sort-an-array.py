class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        k=len(nums)
        res=[]
        heapify(nums)
        for i in range(k):
            res.append(heappop(nums))
        return res 
        