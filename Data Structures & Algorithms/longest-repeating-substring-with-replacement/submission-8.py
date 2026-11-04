class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_map = {}
        max_len = 0

        l = 0
        max_ctr = 0
        for r in range(len(s)):
            curr_char = s[r]
            window_map[curr_char] = 1 + window_map.get(curr_char, 0)

            window = r - l + 1
            max_ctr =  max(window_map[curr_char], max_ctr)
            replacements = window - max_ctr

            if replacements <= k:
                max_len = max(window, max_len)

            while replacements > k:
                window_map[s[l]] = window_map.get(s[l], 0) - 1

                l+=1
                window = r - l + 1
                max_ctr =  max(window_map[curr_char], max_ctr)
                replacements = window - max_ctr
        
        return max_len
