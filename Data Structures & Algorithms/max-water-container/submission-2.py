class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        
        l,r = 0,n-1

        while l<r:
            min_h = min(heights[l],heights[r])
            dist = r-l
            area = min_h * dist
            max_area = max(area , max_area)

            if min_h==heights[l]:
                l+=1
            else:
                r-=1
        return max_area