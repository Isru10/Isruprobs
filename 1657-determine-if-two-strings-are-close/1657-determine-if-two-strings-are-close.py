class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len (word1 )!=len (word2):
            return False 
        f1=Counter (word1)
        f2=Counter (word2)
        if set (f1.keys())!=set (f2.keys()):
            return False 
        f1=dict(sorted (f1.items(), key=lambda item : item[1]))
        f2=dict(sorted (f2.items(), key=lambda item : item[1]))
        return [f for f in f1.values ()]== [f for f in f2.values ()] 