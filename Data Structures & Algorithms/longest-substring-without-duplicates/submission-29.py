class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # 'z' : 0
        max_len = 0
        l = 0

        for r in range(len(s)):
            curr_char = s[r]

            if curr_char in char_map:
                l = max(char_map[curr_char] + 1, l)

            char_map[curr_char] = r
            
            max_len = max(r-l+1, max_len)

        
        return max_len
