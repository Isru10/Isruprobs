class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        t=set(ransomNote)
        for i in t :
            if ransomNote.count(i)>magazine.count(i) or i not in magazine :
                return False 
        return True 