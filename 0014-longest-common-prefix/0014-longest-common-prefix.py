class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=''
        v=sorted(v)
        f=v[0]
        l=v[-1]
        for i  in range( min( len (f), len (l))):
            if f[i]!=l[i]:
                return ans 
            ans+=f[i]
        return ans
