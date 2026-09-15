class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range (len(nums)):
            left = i - 1 # -1
            right = i + 1 # 1
            product = 1

            # except 0
            while left >= 0:
                product *= nums[left]
                left -= 1

            while right < len(nums):
                product *= nums[right]
                right += 1
            
            output.append(product)

        return output
            