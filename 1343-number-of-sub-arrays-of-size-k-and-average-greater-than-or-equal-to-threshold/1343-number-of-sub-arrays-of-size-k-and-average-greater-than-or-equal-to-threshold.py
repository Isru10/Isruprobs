class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        win=sum(arr[:k-1])
        cnt=0
        for l in range(len(arr)-k+1):
            win+=arr[l+k-1]
            if win/k >=threshold :
                cnt+=1
            win-=arr[l]
        return cnt 