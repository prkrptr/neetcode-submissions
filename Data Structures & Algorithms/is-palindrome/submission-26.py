class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            while s[l].isalnum() == False and l < r:
                l+=1
            while s[r].isalnum() == False and l < r:
                r-=1

            
            char_l = s[l].lower()
            char_r = s[r].lower()

            r-=1
            l+=1
            if char_l != char_r:
                return False
        
        return True