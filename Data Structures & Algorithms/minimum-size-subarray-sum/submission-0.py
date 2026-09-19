class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_len = 1000001
        sum_num = 0
        for r in range(len(nums)):
            sum_num += nums[r]

            while sum_num >= target:
                min_len = min(min_len, r-l+1)

                sum_num -= nums[l]
                l+=1
        if min_len == 1000001:
            return 0

        return min_len             