class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l=int(len(arr)*0.05)
        for i in range(l):

            arr.remove(max(arr))
            arr.remove(min(arr))
        s=sum(arr)
        return s/len(arr)