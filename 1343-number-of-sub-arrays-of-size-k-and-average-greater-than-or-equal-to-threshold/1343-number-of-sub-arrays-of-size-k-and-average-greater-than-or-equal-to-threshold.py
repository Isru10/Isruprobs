class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        win=sum(arr[:k-1])
        cnt=0
        l=0
        for r in range(len(arr)-k+1):
            win+=arr[r+k-1]
            if win/k >=threshold :
                cnt+=1
            win-=arr[r]
            
        return cnt 