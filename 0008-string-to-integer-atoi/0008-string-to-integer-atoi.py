class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s :
            return 0
        sign=-1 if s[0]=='-' else 1
        if s[0] in ['-','+']:
            s=s[1:]
        res,i=0, 0
        while i<len(s) and s[i].isdigit():
            res=10*res + int(s[i]) 
            i+=1
        res*=sign
        return max(min(res,2**31-1) , -2**31)
        