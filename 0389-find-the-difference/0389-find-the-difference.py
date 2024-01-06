from collections import *

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ds=Counter (s)
        dt=Counter(t)
        for i,n in enumerate(dt):
            if  not (n in ds and dt[n] ==ds[n]): 
                return str(n)
                