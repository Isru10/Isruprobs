class Solution:
    def countBits(self, n: int) -> List[int]:
        if n ==0 :
            return [0]
        dpa=[0 for i in range(n+1)]
        dpa[1]=1
        for i in range(2, n+1):
            if i %2==0:
                dpa[i]=dpa[i//2]
            else:
                dpa[i]=dpa[i//2]+1
            
        return dpa