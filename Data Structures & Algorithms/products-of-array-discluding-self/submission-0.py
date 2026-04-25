import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        new = []
        for i in range(0,len(nums)):
            new = nums[:i]+nums[i+1:len(nums)]
            n = math.prod(new)
            res.append(n)
        
        return res