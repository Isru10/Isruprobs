class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        ms={}
        mp={}
        if len (s)!=len(pattern):
            return False
        for cp, cs in zip (  pattern , s):
            if cp in mp:
                if mp[cp]!=cs:
                    return False
            else:
                mp[cp]=cs
            if cs in ms:
                if ms[cs]!=cp:
                    return False
            else:
                ms[cs]=cp
                
        return True 