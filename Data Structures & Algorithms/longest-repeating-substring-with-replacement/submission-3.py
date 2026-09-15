class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        max_length = 0
        max_freq = 0
        l = 0
        
        for r in range(len(s)):
            curr_char = s[r]
            if curr_char in char_map:
                char_map[curr_char] +=1
            else:
                char_map[curr_char] = 1
            
            max_freq = max(max_freq, char_map[curr_char])
            window = r - l + 1

            replacements = window - max_freq

            if replacements > k: #invalid 2 > k = 1 (need to move left)
                char_map[s[l]] -= 1
                l +=1
            
            if replacements <= k:
                max_length = max(max_length, window)

        return max_length


                