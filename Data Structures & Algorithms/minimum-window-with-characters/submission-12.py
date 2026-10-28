class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""


        freq_map = {}

        for c in t:
            freq_map[c] = 1 + freq_map.get(c, 0)
        
        char_map = {}
        res = [float('inf'), [-1,-1]]
        have = 0
        need = len(freq_map)
        l = 0
        for r in range (len(s)):
            curr_char = s[r]
            if curr_char in t:
                char_map[curr_char] = 1 + char_map.get(curr_char, 0)
                
                if char_map[curr_char] == freq_map[curr_char]:
                    have+=1
            
            
                

            while have == need:
                if r-l+1 < res[0]:
                    res[0] = min(res[0], r-l+1)
                    res[1][0] = l
                    res[1][1] = r

                if s[l] in t:
                    char_map[s[l]] = char_map.get(s[l], 0) - 1

                    if char_map[s[l]] < freq_map[s[l]]:
                        have -= 1
                
                l+=1
                

        return "" if res[0] == float('inf') else s[res[1][0]:res[1][1]+1]









        

