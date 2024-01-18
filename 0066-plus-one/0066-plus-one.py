class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        d=d[::-1]
        one=1
        i=0
        while one :
            if i<len(d):
                if d[i]==9:
                    d[i]=0
                else:
                    d[i]+=1
                    one=0
            else: 
                d.append(1)
                one=0
            i+=1
        return d[::-1]