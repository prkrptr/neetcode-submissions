class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        max_length = 0

        l = 0
        window = 0
        max_freq = 0
        for r in range(len(s)):
            curr_char = s[r]

            char_map[curr_char] = char_map.get(curr_char,0) + 1

            max_freq = max(max_freq, char_map[curr_char])
            window = r - l +1
            replacements = window - max_freq
            if replacements <= k:# valid
                max_length= max(max_length, window)

            if replacements > k: #invalid
                char_map[s[l]] -=1
                l += 1

        return max_length

