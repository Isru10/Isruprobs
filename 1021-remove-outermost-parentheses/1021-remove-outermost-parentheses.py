class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        index=0
        openpar=0
        n=len(s)
        res=""
        while index <n:
            if s[index]=="(":
                if openpar>=1:
                    res+=s[index]
                openpar+=1
            else :
                openpar-=1
                if openpar>=1:
                    res+=s[index]
            index+=1
        return res