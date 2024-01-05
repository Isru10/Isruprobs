class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        window=str(num)[:k]
        count=0
        if (num % int(window)==0 ):
            count+=1
        for i in range(1,len(str(num))-k+1):
            window=str(num)[i:k+i]
            if (int(window)!=0 and  num%int(window)==0):
                count+=1
        return count 