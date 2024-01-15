class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        seen={}
        result=0
        for i , r in enumerate (s):
            if (seen . get(r,-1) >=start):
                start=seen[r]+1
            result = max(result , i-start+1)
            seen[r]=i
        return result 