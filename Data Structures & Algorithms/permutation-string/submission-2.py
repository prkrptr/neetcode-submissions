class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_map = {}

        for c in s1:
            count_map[c] = 1 + count_map.get(c,0) 

        window_map = {}
        target_window_size = len(s1)
        l = 0

        for r in range(len(s2)):
            window_map[s2[r]] = 1 + window_map.get(s2[r],0)

            curr_window_size = r - l + 1
            if curr_window_size == target_window_size:
                if count_map == window_map:
                    return True
                window_map[s2[l]] -= 1
                if window_map[s2[l]] == 0:
                    del window_map[s2[l]]
                l +=1
        
        return False
