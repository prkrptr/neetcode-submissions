class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        l, r = 0, len(heights)-1
        while l < r:
        
            min_num = min(heights[l], heights[r])
            curr_area = min_num * (r-l)
            max_amt = max(max_amt, curr_area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_amt
        
