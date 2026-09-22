class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        l = 0
        count_ones = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count_ones +=1

            window = r - l + 1

            while window - count_ones > k:
                if nums[l] == 1:
                    count_ones -= 1
                l += 1
                window = r - l + 1
            
            if window - count_ones <= k:
                max_len = max(max_len, window)

        return max_len

                
            
            

            
