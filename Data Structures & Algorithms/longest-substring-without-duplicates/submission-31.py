class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        char_map = {}
        for r in range(len(s)):
            curr_char = s[r]

            if curr_char in char_map: # found a duplicate 
                l = max(char_map[curr_char]+1, l)
                # do something
            
            char_map[curr_char] = r

            max_len = max(max_len, r-l+1)

        return max_len
