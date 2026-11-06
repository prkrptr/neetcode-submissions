class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)-1

        while l < r:
            min_height = min(heights[l], heights[r])
            width = r - l 

            area = min_height * width

            max_area = max(max_area, area)

            if heights[l] <= heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            
        
        return max_area