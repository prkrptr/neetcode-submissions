class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        lookup = []
        for r in range(len(s)):
            while s[r] in lookup:
                lookup.remove(s[l])
                l+=1
            
            lookup.append(s[r])
            max_len = max(max_len, r-l+1)
        
        return max_len