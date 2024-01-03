class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a=1
        b=max(piles)
        while a<b :
            mid=(a+b)//2
            c=0
            for j in piles :
                c+=math.ceil(j/mid)
            if c>h:
                a=mid+1
            else:
                b=mid
        return a
             