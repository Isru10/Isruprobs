class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        x=0
        for  i in words:
            if s[x:x+len(i)]!=i:
                return False 
            x+=len(i)
            if x==len(s):
                return True
        return False
     