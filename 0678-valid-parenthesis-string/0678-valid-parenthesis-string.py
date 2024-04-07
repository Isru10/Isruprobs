class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt=0
        stack=[]
        star=[]
        for i, char in enumerate(s):
            if char =="(":
                stack.append(i)
            elif char=="*":
                star.append(i)
            elif char==")":
                if stack :
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stack and star:
            if stack[-1]<star[-1]:
                stack.pop()
                star.pop()
            else:
                break 
        return not stack
            
        
