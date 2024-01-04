class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[        ]
        n=len(nums)
        ptr1=0
        while ptr1<n-2 :
            if ptr1>0 and nums [ptr1] == nums[ptr1-1]:
                ptr1+=1
                continue 
            if nums [ptr1]>0:
                break
            ptr2, ptr3=ptr1+1,n-1
            while ptr2<ptr3:
                sum_=nums[ptr1]+nums[ptr2]+nums[ptr3]
                if sum_==0:
                    ans.append([nums[ptr1],nums[ptr2],nums[ptr3]])
                    ptr2+=1
                    ptr3-=1
                    while ptr2<ptr3 and nums[ptr2]==nums [ptr2-1]:
                        ptr2+=1
                    while ptr2<ptr3 and nums[ptr3]==nums [ptr3+1]:
                        ptr3-=1
                elif sum_<0:
                    ptr2+=1
                else:
                    ptr3-=1
            ptr1+=1
        return ans