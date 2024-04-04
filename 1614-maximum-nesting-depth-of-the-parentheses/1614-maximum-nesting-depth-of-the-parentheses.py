class Solution:
    def maxDepth(self, s: str) -> int:
        stk=[]
        res=0
        for i in s:
            if i =="(":
                stk.append(i)
                res=max(res,len(stk))
            elif i==")":
                stk.pop()
        return res
                