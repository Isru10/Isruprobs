from heapq import *
class Solution:
    def maxScore(self, nums: List[int], muls: List[int], k: int) -> int:
        t=m = 0
        heap=[]
        for mul , num in sorted(zip(muls, nums ) , reverse=True):
            heappush(heap, num )
            t+=num
            if len(heap)> k :
                t-=heappop(heap)
            if len(heap)==k :
                m=max(m, t*mul)
        return m
            