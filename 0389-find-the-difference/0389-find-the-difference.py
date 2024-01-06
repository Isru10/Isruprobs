class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in (t):
            if not ((i in s) and( (t.count(i) ) == (s.count(i) ) )):
                return i