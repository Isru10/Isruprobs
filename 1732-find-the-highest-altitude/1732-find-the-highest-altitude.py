class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mn=0
        cn=0
        for i in range (len (gain)):
            if mn < cn+gain [i]:
                mn =cn+gain [i]
            cn+=gain[i]
        return mn 