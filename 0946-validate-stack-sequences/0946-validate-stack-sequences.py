class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        s=[]
        for n in pushed:
            s.append(n)
            while s and i<len(popped) and s[-1]==popped[i]:
                s.pop()
                i+=1
        return True if not s else False