class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_freq = 0
        char_map = {} # X: 0, Y: 0
        l = 0

        for r in range (len(s)):
            curr_char = s[r]

            char_map[curr_char] = 1 + char_map.get(curr_char, 0)

            max_freq = max(max_freq, char_map[curr_char])

            window_size = r-l+1

            if window_size - max_freq <= k:
                max_len = max(max_len, window_size)

            while window_size - max_freq > k:
                char_map[s[l]] -= 1
                l+=1
                window_size = r-l+1
            
        return max_len



