class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
            
        t_map = {}

        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        window = {}
        result = [0,0,100001] # could be improved further 
        l = 0
        have = 0
        need = len(t_map)

        for r in range (len(s)):
            curr_char = s[r]
            if curr_char in t_map:
                window[curr_char] = 1 + window.get(curr_char, 0)
                if window[curr_char] == t_map[curr_char]:
                    have +=1

            # if window is valid
            while have == need:
                if r-l+1 <= result[2]:
                    result[0]= l
                    result[1]= r
                    result[2] = r-l+1
                if s[l] in t_map:
                    window[s[l]] -= 1
                    if window[s[l]] < t_map[s[l]]:
                        have -=1
                l+=1
            
        if result[2] < 100001:
            return s[result[0]:result[1]+1]
        else:
            return ""

            
        
