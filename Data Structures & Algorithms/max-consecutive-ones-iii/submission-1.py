class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = {}
        max_length = 0
        l = 0

        for r in range(len(nums)):
            curr_num = nums[r]

            window[curr_num] = 1 + window.get(curr_num, 0)
            
            if r-l+1 - window.get(1, 0) <= k:
                max_length = max(r-l+1, max_length)

            while r-l+1 - window.get(1, 0) > k:
                window[nums[l]] -= 1
                l+=1

        return max_length


