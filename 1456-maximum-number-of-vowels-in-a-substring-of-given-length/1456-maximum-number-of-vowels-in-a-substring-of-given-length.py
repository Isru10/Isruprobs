class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels='aeiou'
        window=res=0
        for i in range(len (s)):
            window +=s[i] in vowels
            if i >=k:
                window -=s[i - k ] in vowels
            res= max(window , res )
        return res 