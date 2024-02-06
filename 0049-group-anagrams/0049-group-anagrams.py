from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for word in strs:
            sortedword=''.join(sorted(word))
            ans[sortedword].append(word)
        return ans.values()