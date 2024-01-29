class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q=collections.deque()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in q:
                q.popleft()
                l+=1
            q.append(s[i])
            res=max(res, i-l+1)
        return res 