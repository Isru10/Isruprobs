class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer =0 
        left =0
        zeros=0
        ones=0
        for right in range (len (nums )):
            if nums [right ]==0:
                zeros+=1
                while zeros>1:
                    if nums[left ]==0:
                        zeros-=1
                    else:
                        ones-=1
                    left +=1
            else:
                ones+=1
            answer=max(answer, ones )
        return answer if zeros ==1 else answer -1