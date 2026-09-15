class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(set(nums)) 
        arr = []
        count = 0
        if len(nums) > 0:
            count = 1

        # [9,1,4,7,3,-1,0,5,8,-1,6] -1, 0, 1,3,4,5,6,7,8,9
        for i in range (len(nums_sorted)-1):
            if abs(nums_sorted[i+1] - nums_sorted[i]) == 1:
                count += 1
            else:
                arr.append(count)
                count = 1 #reset
        arr.append(count)
        return max(arr)
