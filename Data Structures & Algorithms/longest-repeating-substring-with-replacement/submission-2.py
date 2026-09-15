class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {} # tracks character and count
        l = 0 
        max_length = 0
        max_freq = 0
        for r in range(len(s)):
            curr_char = s[r]

            if curr_char in char_map:
                char_map[curr_char] += 1
            else:
                char_map[curr_char] = 1

            max_freq = max(max_freq, char_map[curr_char])
            
            window_size = r - l + 1

            replacements = window_size - max_freq

            if replacements > k:
                char_leaving = s[l]
                char_map[char_leaving] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
                
            
        return max_length
                    