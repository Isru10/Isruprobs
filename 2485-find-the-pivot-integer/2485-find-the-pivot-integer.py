class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1: return 1
        if n==0:return 0
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        for i in range(len(arr)):
            if sum(arr[:i])==sum(arr[i+1:]):
                return arr[i]
        return -1
            
        