class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        de=[0]*101
        conv=1950
        for l in logs :
            de[l[0]-conv]+=1
            de[l[1]-conv]-=1
        runs=0
        mp=0
        year=1950
        for i , d in enumerate(de):
            runs+=d
            if runs>mp:
                mp=runs
                year=conv+i
        return year
        