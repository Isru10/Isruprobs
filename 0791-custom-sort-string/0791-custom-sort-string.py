class Solution:
    def customSortString(self, order: str, s: str) -> str:
        scount=Counter(s)
        sarr=[]
        for i in order:
            if i in scount:
                sarr.append(i*scount[i])
                del scount[i]
        for i in scount:
            sarr.append(i*scount[i])
        return "".join(sarr)         
       