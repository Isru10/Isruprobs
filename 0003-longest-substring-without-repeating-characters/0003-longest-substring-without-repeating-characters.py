class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        q=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in q:
                    q.remove(s[l])
                    l+=1
            q.add(s[r])
            res=max(res,r-l+1)

        return res
        
