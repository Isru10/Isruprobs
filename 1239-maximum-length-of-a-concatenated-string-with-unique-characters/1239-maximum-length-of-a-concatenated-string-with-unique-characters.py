class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isuni(subs):
            return len(subs)==len(set(subs))
        def bt(start, cs):
            nonlocal maxl
            if isuni(cs):
                maxl=max(maxl, len(cs))
            for i in range(start, len(arr)):
                bt(i+1, cs+arr[i] )
        maxl=0
        bt(0,'')
        return maxl
