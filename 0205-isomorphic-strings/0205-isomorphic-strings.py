from collections import Counter 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len ( s)!=len(t):
            return False
        ms={}
        mt={}
        for cs, ct in zip (s, t):
            if cs in ms :
                if ms[cs]!=ct:
                    return False
            else:
                ms[cs]=ct
            if ct in mt :
                if mt[ct]!=cs:
                    return False
            else:
                mt[ct]=cs
        return True
            