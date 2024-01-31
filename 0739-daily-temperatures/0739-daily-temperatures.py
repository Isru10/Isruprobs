class Solution:
    def dailyTemperatures(self, te: List[int]) -> List[int]:
        res=[0]*len(te)
        stack=[]#[temp, ind]
        for i, t in enumerate(te):
            while stack and t>stack[-1][0]:
                stkT, stkid=stack.pop()
                res[stkid]=(i-stkid)
            stack.append([t,i])
        return res
                