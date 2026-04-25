class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        
        longe = 0
        for i in s:
            if i-1 not in s:
                x = i
                count = 1
                while x+1 in s:
                    count+=1
                    x = x+1
                longe = max(count,longe)
        return longe