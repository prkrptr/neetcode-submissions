class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        l = 0

        for r in range(len(s)):
            curr_char = s[r]

            if curr_char in char_map and char_map[curr_char] >= l:
                l = char_map[curr_char] + 1

            char_map[curr_char] = r
            max_length = max(max_length, r-l+1)

        return max_length