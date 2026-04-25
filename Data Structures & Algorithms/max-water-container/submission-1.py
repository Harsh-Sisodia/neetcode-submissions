class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        
        for i in range(0,n):
            for j in range(i+1,n):
                l,r=i,j
                min_h=min(heights[i],heights[j])
                dist = r-l
                area = min_h*dist
                max_area = max(max_area,area)
        return max_area             
