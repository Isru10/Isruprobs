class Solution:
    def removeStars(self, s: str) -> str:
        outarray=[  ]
        for i in range(len (s )):
            if s[i]=='*':
                outarray.pop()
            else:
                outarray.append(s[i])
        return ''.join(outarray)