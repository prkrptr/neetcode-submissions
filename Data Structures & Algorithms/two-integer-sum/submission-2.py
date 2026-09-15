class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total_sum = 0
        arr = {}
        i = 0

        for i in range (len(nums)):
            check = target - nums[i]
            if check in arr:
                return [arr[check],i]

            arr[nums[i]] = i
        

