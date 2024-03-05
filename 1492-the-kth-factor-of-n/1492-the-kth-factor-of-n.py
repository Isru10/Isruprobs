class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        reserve=n
        temp=n
        arr=[]
        for i in range(n):
            if temp%reserve==0:
                arr.append(reserve)
            reserve-=1
        arr.sort()
        if len(arr)>=k:
            return arr[k-1]
        else:
            return -1