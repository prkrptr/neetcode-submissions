class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_map = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            curr_char = s[r]

            if curr_char in window_map:
                
                l = max(window_map[curr_char]+1, l)
            
            max_len = max(r - l + 1 ,max_len)
            window_map[curr_char] = r

        return max_len
            
