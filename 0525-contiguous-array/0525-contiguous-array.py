class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count={0:-1}
        maxlen,countdif =0,0
        for i,num in enumerate(nums):
            if num==1:
                countdif+=1
            if num==0:
                countdif-=1
            if countdif in count:
                maxlen=max(maxlen, i-count[countdif])
            else:
                count[countdif]=i
        return maxlen