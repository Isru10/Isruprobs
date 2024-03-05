class Solution:
    def partitionString(self, s: str) -> int:
        t=''
        res=[]
        for i in s:
            if i not in t :
                t+=i
            else:
                res.append(t)
                t=i
        if t :
            res.append(t)
        return len(res)