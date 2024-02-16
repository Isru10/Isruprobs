class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c=Counter(arr)
        v=list(c.values())
        v.sort()
        cnt=0
        for i in range(len(v)):
            if k>v[i]:
                k-=v[i]
                v[i]=0
            else:
                v[i]-=k
                k=0
            if v[i]!=0:
                cnt+=1
        return cnt