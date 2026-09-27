class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}

        l = 0
        max_len = 0
        for r in range(len(s)):
            curr_char = s[r]

            if curr_char in char_map and char_map[curr_char] >= l:
                l = char_map[curr_char] + 1

            
            char_map[curr_char] = r
            max_len = max(max_len, r-l+1)



        return max_len