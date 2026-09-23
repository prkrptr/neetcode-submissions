class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        freq_map = {}

        for c in t:
            freq_map[c] = 1 + freq_map.get(c, 0)

        have = 0
        need = len(freq_map)
        res = [-1,-1]
        res_len = float('inf')
        window_map = {}
        l = 0 
        for r in range(len(s)):

            curr_char = s[r]

            if curr_char in t:
                window_map[curr_char] = 1 + window_map.get(curr_char, 0)
                if window_map[curr_char] == freq_map[curr_char]:
                    have +=1

            while have == need:

                if r-l+1 <= res_len:
                    res_len = min(r-l+1, res_len)
                    res[0] = l
                    res[1] = r

                if s[l] in t:
                    window_map[s[l]] = window_map.get(s[l], 0) - 1
                    if window_map[s[l]] < freq_map[s[l]]:
                        have -=1
                l += 1

        return "" if res_len == float('inf') else s[res[0]:res[1]+1]

        


