class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel='aeiou'
        l=0
        count=0
        res=0
        for i in range( len ( s )):
            if s[i] in vowel : count+=1
            
            if i-l+1>k:
                if s[l] in vowel  : 
                    count-=1
                l+=1
            res=max(res,count)
        return res