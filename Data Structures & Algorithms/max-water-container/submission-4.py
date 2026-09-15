class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r:
            min_bar = min(heights[l], heights[r])
            curr_amt = (r-l) * min_bar 
            max_area = max(curr_amt, max_area)

            if heights[l] < heights[r]:
                l+= 1
            else:
                r-=1
            
        return max_area