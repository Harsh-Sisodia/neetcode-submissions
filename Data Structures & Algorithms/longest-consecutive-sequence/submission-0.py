class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longe = 0
        
        

        for i in range(0,len(nums)):
            if nums[i]-1 in nums:
                continue
            count = 1
            last = nums[i]
            start = 0
            while start==0:
                if last+1 in nums:
                    count +=1
                else:
                    start=1
                last+=1
            longe = max(count,longe)
        
        return longe

            
        


        return 0