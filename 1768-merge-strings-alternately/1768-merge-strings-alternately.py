class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        l=[]
        i=0
        j=0
        while i<len(w1) or j<len(w2):
            if i<len(w1):
                l.append(w1[i])
            if j<len(w2):
                l.append(w2[j])
            i+=1
            j+=1
        return ''.join(l)