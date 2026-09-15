class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        track = set()
        max_len = 0
        for r in range(len(s)):
            while s[r] in track: #moves until no dupes in track
                track.remove(s[l])
                l +=1
            
            track.add(s[r])
            max_len = max(max_len, r-l+1)
    
        return max_len

