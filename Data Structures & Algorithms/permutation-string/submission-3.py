class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}

        for c in s1:
            freq_map[c] = 1 + freq_map.get(c, 0)

        l = 0

        window_map = {}
        window_size = 0
        for r in range(len(s2)):
            curr_char = s2[r]
            window_map[curr_char] = 1 + window_map.get(curr_char, 0)
            window_size +=1

            while window_size > len(s1):
                window_map[s2[l]] = window_map.get(s2[l], 0) - 1
                if window_map[s2[l]] == 0:
                    del window_map[s2[l]]
                window_size -= 1
                l+=1
            
            
            if window_map == freq_map:
                return True
            
        
        return False
    
            