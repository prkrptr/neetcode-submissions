class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        l = 0
        num_ones = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                num_ones +=1
            
            window = r - l + 1

            replacements = window - num_ones

            if replacements <= k:
                max_length = max(max_length, window)

            while replacements > k:
                if nums[l] == 1:
                    num_ones -= 1
                
                l+=1
                window = r - l + 1
                replacements = window - num_ones

        return max_length



                
        
