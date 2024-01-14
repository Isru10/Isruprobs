from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs=='':
            return [['']]
        d=defaultdict(list)
        for i in strs:
            d[hash(tuple(sorted(Counter(i).items())))].append(i)
        return d.values()
        