class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                num_sum = nums[l] + nums[r]

                if num_sum == target:
                    arr.append([nums[i],nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                    while nums[r] == nums[r+1] and l < r:
                        r-=1
                elif num_sum < target:
                    l+=1
                else:
                    r-=1

        return arr     

            

