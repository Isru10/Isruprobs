class Solution:
    def maxDepth(self, s: str) -> int:
        r=0
        res=0
        l=0
        for i in s:
            if i =="(":
                r+=1
                res=max(res,r)

            elif i==")":
                r=r-1
        return res
                