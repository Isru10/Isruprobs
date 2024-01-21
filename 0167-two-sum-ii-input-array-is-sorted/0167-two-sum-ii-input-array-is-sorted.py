class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l=0
        r=len(n)-1
        while l<r :
            cs=n[l]+n[r]
            if cs<t:
                l+=1
            elif( cs>t):
                r-=1
            else:
                return [l+1, r+1]
        return []
        