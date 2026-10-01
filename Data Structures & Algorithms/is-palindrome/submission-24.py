class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        i = 0
        j = len(s)-1

        while i < j:
            char_i = s[i].lower()
            char_j = s[j].lower()
            

            while char_i.isalnum() == False and i < j:
                i+=1
                char_i = s[i].lower()

            while char_j.isalnum() == False and i < j:
                j-=1
                char_j = s[j].lower()

            if s[i].lower() != s[j].lower():
                return False

            i+=1
            j-=1
            
        return True





