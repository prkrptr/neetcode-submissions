class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_ones = 0
        window = 0
        l = 0
        max_len = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count_ones+=1
            
            window = r - l + 1

            replacements = window - count_ones
            if replacements <= k:
                max_len = max(max_len, window)

            while replacements > k:

                if nums[l] == 1:
                    count_ones -=1
                
                l+=1
                window = r - l + 1
                replacements = window - count_ones

        return max_len

