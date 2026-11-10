class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        char_map = {}

        for c in s1:
            char_map[c] = 1+char_map.get(c,0)
        
        l = 0
        window_map = {}
        need = len(char_map)
        have = 0

        
        for r in range(len(s2)):
            curr_char = s2[r]
            
            window_map[curr_char] = 1 + window_map.get(curr_char, 0)

           

            while r-l+1 > len(s1):                
                window_map[s2[l]] = window_map.get(s2[l],0) - 1

                if window_map[s2[l]] == 0:
                    del window_map[s2[l]]
                
                l+=1
            
            if window_map == char_map:
                return True

        return False
                
            
