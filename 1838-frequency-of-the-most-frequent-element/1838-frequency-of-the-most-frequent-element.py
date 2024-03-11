class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        q=collections.deque()
        best=1
        q.append(nums[0])
        used=0
        for r in range(1,N):
            used+=len(q)*(nums[r]-q[-1])
            q.append(nums[r])
            while used>k:
                x=q.popleft()
                used-=nums[r]-x
            best=max(best,len(q))
        return best