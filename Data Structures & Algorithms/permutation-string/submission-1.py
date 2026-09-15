class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_map = {}        
        for i in range(len(s1)):
            if s1[i] in count_map:
                count_map[s1[i]] +=1
            else:
                count_map[s1[i]] = 1
        
        window_map ={}
        target_window_size = len(s1) 
        l = 0
        for r in range(len(s2)):
            if s2[r] in window_map:
                window_map[s2[r]] +=1
            else:
                window_map[s2[r]] = 1
            
            curr_window_size = r - l + 1
            if curr_window_size == target_window_size:
                if count_map == window_map:
                    return True
                window_map[s2[l]] -= 1
                if window_map[s2[l]] == 0:
                    del window_map[s2[l]] 
                l += 1
                

        
        return False