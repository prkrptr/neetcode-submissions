class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        
        max_freq = 0
        max_len = 0
        l = 0
        for r in range(len(s)):
            curr_char = s[r]
            freq_map[curr_char] = 1 + freq_map.get(curr_char, 0) 

            max_freq = max(max_freq, freq_map[curr_char])

            window = r-l+1
            replacements = window - max_freq
            if replacements <= k:
                max_len = max(max_len, window)

            if replacements > k:
                freq_map[s[l]] = freq_map.get(s[l],0)-1
                l+=1

        return max_len
                
            
