class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        tot=0
        mul=1
        for i , c in enumerate(s):
            if c=="(":
                mul*=2
            elif c ==")":
                if s[i-1]=="(":
                    tot+=mul//2
                mul= mul//2
        return tot 