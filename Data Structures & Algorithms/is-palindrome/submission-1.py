class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = self.to_alphanumeric(s)

        return string == string[::-1]
    
    def to_alphanumeric(self, s: str) -> str:
        new_string = []
        string = str.lower(s)
        # retain only alphanumeric
        for char in string:
            if char <= "z" and char >= "a" or char <= "9" and char >= "0":
                new_string.append(char)
        return "".join(new_string)
