class Solution:
    def frequencySort(self, s: str) -> str:
        charcount=Counter (s)
        sortedchar=sorted(charcount, key=charcount.get, reverse=True )
        result=''
        for char in sortedchar:
            result+=char*charcount[char]
        return result