class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #checks

        str_list = list("".join((s.lower()).split()))
        new_str = ""
        for char in str_list:
            if char.isalnum():
                new_str += char

        return new_str == new_str[::-1]




