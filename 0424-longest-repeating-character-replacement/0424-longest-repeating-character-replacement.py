class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mxlen=0
        fre=0
        start=0
        h={}
        for end, char in enumerate (s ):
            h[char]=h.get(char,0)+1
            fre=max(fre, h[char])
            if (end-start+1)-fre>k:
                h[s[start]]-=1
                start+=1
            mxlen=max(mxlen, end-start+1)
        return mxlen