class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        minw=float('inf')
        current=0
        for i in range(len(b)):
            if b[i]=='W':
                current+=1
            if i-k>=0 and b[i-k]=='W':
                current-=1
            if i-k+1>=0:
                minw=min(minw, current)
            i+=1
        return minw