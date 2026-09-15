class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""


        t_map = {}

        for char in t:
            t_map[char] = 1 + t_map.get(char, 0)
        
        l = 0
        window_map = {}
        have = 0
        need = len(t_map)
        substring_length = 100001 # or set to infinity
        substring = [0,0]

        for r in range(len(s)):
            curr_char = s[r]

            if curr_char in t_map:
                window_map[curr_char] = 1 + window_map.get(curr_char, 0)
                if window_map[curr_char] == t_map[curr_char]:
                    have +=1


            while have == need:
                if r - l + 1 <= substring_length:
                    substring_length = r-l+1
                    substring[0] = l
                    substring[1] = r+1

                # if valid we need to move l to make it invalid
                if s[l] in t_map:
                    window_map[s[l]] -=1
                    if window_map[s[l]] < t_map[s[l]]:
                        have -=1

                l+=1
        return s[substring[0] :substring[1]] 
