class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check_map = {}

        for c in s1:
            check_map[c] = 1 + check_map.get(c,0)

        string_map = {}
        l = 0

        for r in range(len(s2)):
            curr_char = s2[r]
            string_map[curr_char] = 1 + string_map.get(curr_char,0)
            

            if r - l + 1 > len(s1):
                string_map[s2[l]] = string_map.get(s2[l],0) - 1
                if string_map[s2[l]] == 0:
                    del string_map[s2[l]]
                l+=1
            

            if check_map == string_map:
                return True
        
        return False





