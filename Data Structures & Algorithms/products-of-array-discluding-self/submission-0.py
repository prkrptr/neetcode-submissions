class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate through entire nums list
        products = [0] * len(nums)
        left = [0] * len(nums)
        right = [0] * len(nums)
        left[0] = 1
        right[len(nums)-1] = 1 

        #construct left array
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        #construct right array
        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]

        for i in range(len(nums)):
            products[i] = left[i] * right[i]
        
        return products


