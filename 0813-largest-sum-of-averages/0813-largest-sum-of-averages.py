class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        cache={}
        def dfs(i,k):
            if k==1:
                return sum(nums[i:])/len(nums[i:])
            if (i,k) in cache:
                return cache[(i,k)]
            cursum=0
            size=0
            curavg=0
            res=float("-inf")
            for j in range(i,len(nums)-k+1):
                cursum+=nums[j]
                size+=1
                curavg=cursum/size
                rightavg=dfs(j+1,k-1)
                tot=curavg+rightavg
                res=max(tot,res)
            cache[(i,k)]=res
            return res
        return dfs(0,k)
        