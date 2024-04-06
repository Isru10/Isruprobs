class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        final=[]
        left=[]
        cnt=0
        for char in  s:
            if char=='(':
                cnt+=1
                final.append(char)
                left.append(len(final)-1)
            elif char==')':
                if cnt-1>=0:
                    final.append(char)
                    cnt-=1
            else:
                final.append(char)
        while cnt>0:
            final.pop(left[-1])
            left.pop()
            cnt-=1
            
                
        return "".join (final )
       