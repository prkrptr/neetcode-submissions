class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}
        for c in s1:
            freq_map[c] = 1 + freq_map.get(c, 0)

        check_map = {}

        l = 0
        for r in range (len(s2)):
            curr_char = s2[r]

            check_map[curr_char] = 1 + check_map.get(curr_char, 0)
            window = r - l + 1

            while window > len(s1):
                check_map[s2[l]] = check_map.get(s2[l], 0) - 1

                if check_map[s2[l]] == 0:
                    del check_map[s2[l]]
                l+=1
                window = r - l + 1
            
            if freq_map == check_map:
                return True
        return False


            
