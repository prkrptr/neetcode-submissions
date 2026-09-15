class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}

        for i, num in enumerate(nums):
            check = target - num
            if check in seen_nums:
                return [seen_nums[check],i]

            seen_nums[num] = i

            