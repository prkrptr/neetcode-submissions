class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            size = 0
            if heights[l] <= heights[r]:
                size = heights[l]
                l += 1  
            else:
                size = heights[r]
                r -= 1 

            curr_water = size * (r - l + 1)

            if curr_water > max_water:
                max_water = curr_water

        return max_water