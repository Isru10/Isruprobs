class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        arr=["0"]*n
        r=n-1
        l=0
        for i in range(n):
            if s[i]=="1" and "1" not in arr:
                arr[r]=s[i]
               
            elif s[i]=="1" and "1" in arr:
                arr[l]=s[i]
                l+=1
             
               
        return "".join(arr)
            