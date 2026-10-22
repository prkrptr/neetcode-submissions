class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}

        for c in s1:
            freq_map[c] = 1 + freq_map.get(c, 0)
            

        char_map = {}
        l = 0

        for r in range (len(s2)):
            curr_char = s2[r]
            char_map[curr_char] = 1 + char_map.get(curr_char, 0)
            
            if r - l + 1 > len(s1):
                char_map[s2[l]] = char_map.get(s2[l],0)-1
                if char_map[s2[l]] == 0:
                    del char_map[s2[l]]
                l+=1

            if char_map == freq_map:
                return True
        
        return False


