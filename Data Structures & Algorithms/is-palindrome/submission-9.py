class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        ctr = 0
        while left < right:

           
            while s[left].lower().isalnum() == False and left < right:
                left += 1

            while s[right].lower().isalnum() == False and right > left:
                right -= 1
            
            if s[left].lower() == s[right].lower():
                ctr +=1
            else:
                return False
            if left == right:
                break

            left += 1
            right -=1

        
        return True







