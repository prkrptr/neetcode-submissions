class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}

        for i in range (len(nums)):
            table[nums[i]] = 1 + table.get(nums[i], 0)
            if table[nums[i]] >= 2:
                return True

        return False