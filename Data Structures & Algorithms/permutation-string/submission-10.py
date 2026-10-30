class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq_map = {}

        for c in s1:
            freq_map[c] = 1 + freq_map.get(c, 0)

        l = 0
        count_map = {}
        for r in range(len(s2)):
            curr_char = s2[r]
            count_map[curr_char] = 1 + count_map.get(curr_char, 0)
            window = r - l + 1

            while window > len(s1):
                count_map[s2[l]] = count_map.get(s2[l], 0) - 1

                if count_map[s2[l]] == 0:
                    del count_map[s2[l]]
                l+=1
                window = r - l + 1


            if freq_map == count_map:
                return True
        return False