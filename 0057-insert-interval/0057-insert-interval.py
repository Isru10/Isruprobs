class Solution:
    def insert(self, i: List[List[int]], ni: List[int]) -> List[List[int]]:
        i.append(ni)
        i.sort(key=lambda x:x[0])
        ns=[i[0]]
        for it in i[1:]:
            if it[0]>ns[-1][1]:
                ns.append(it)
            else:
                ns[-1][1]=max(ns[-1][1],it[1])
        return ns