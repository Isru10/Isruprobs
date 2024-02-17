class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        heap=[]
        for i in range(len(h)-1):
            diff=h[i+1]-h[i]
            if diff >0:
                heapq.heappush(heap,diff)
                if len(heap)>l:
                    b-=heapq.heappop(heap)
                if b<0:
                    return i 
        return len(h)-1