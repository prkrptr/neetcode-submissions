class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) < 2:
            return len(nums)

        nums = sorted(nums)

        ctr = 1 # counted if only 1
        max_ctr = 1
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]: #if consecutive
                ctr += 1
            elif nums[i] == nums[i+1]:
                continue
            else: 
                ctr = 1

            if ctr > max_ctr:
                max_ctr = ctr
        
        return max_ctr
            
            