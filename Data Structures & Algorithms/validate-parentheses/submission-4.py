class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {'}':'{', ')':'(',']':'['}

        for char in s:
            if char in table:
                if not stack or stack[-1] != table[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return not stack