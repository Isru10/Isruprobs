class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        res=0
        while l<r:
            m= (l+r+1)>>1
            if m<=x//m:
                l=m
          
            else:
                r= m-1
        return l