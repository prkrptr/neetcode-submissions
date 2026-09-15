class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_copy = sorted(list(s))
        t_copy = sorted(list(t))
        return "".join(s_copy) == "".join(t_copy)