class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel='aeiou'
        res=0
        l=0
        count=0
        for i in range(len (s)):
            count+=1 if s[i] in vowel else 0
            if i-l+1 > k :
                count-=1 if s[l] in vowel else 0
                l+=1
            res=max(res, count)
        return res