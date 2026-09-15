class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        numSet = set(nums)
        ctr = 1
        max_ctr = 1
        

        for num in numSet:
            if num-1 not in numSet: # start of sequence
                check = num 
                ctr = 1
                while True: # count until u check all seq
                    if check + 1 in numSet:
                        ctr += 1
                        check += 1
                    else:
                        break
                max_ctr = max(ctr, max_ctr)
        
            
            
        return max_ctr