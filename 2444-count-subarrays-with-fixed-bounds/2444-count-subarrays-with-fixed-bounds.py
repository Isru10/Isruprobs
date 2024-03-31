class Solution:
    
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        nums.append(10**20)
        def solve(arr):
            n=len(arr)
            lmn,lmx=-1,-1
            cnt=0
            for i in range(n):
                if arr[i]==minK:
                    lmn=i
                if arr[i]==maxK:
                    lmx=i
                cnt+=min(lmx,lmn)+1
            return cnt
            
        arr=[]  
        cnt=0
        for x in nums:
            if minK<=x<=maxK:
                arr.append(x)
            else:
                cnt+=solve(arr)
                arr=[]
        return cnt