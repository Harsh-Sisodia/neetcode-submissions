class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        else:
            l,r=0,len(nums)-1
            res = nums[0]
            while r>=l:
                mid = l+r+1//2
                res = min(res,nums[mid])
                if nums[mid]>nums[r]:
                    l=mid+1
                else:
                    r=mid-1

        return res
        