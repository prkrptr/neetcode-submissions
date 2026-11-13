class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = 0 

        max_char = 0
        max_len = 0
        for r in range(len(s)):
            curr_char = s[r]

            freq_map[curr_char] = 1 + freq_map.get(curr_char, 0)

            max_char = max(freq_map[curr_char], max_char)

            window = r - l + 1

            replacements = window - max_char 

            if replacements <= k :
                max_len = max(max_len, window)

            while replacements > k and l < r:
                freq_map[s[l]] = freq_map.get(s[l],0) - 1
                l+=1
                window = r-l+1
                max_char = max(freq_map[curr_char], max_char)
                replacements = window - max_char 

        return max_len


