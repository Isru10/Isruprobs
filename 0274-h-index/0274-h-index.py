class Solution:
    def hIndex(self, c: List[int]) -> int:
        i=0
        c.sort(reverse=True)
        
        while i<len(c) and i<c[i] :
            i+=1
        return i