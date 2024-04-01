class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s=[]
        for n in num:
            while s and k>0 and s[-1]>n:
                k-=1
                s.pop()
            
            s.append(n)
        s=s[:len(s)-k]
        res="".join(s).lstrip("0")
        return res if res else "0"
            
  