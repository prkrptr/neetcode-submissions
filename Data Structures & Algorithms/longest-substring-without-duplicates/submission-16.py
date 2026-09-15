class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store
        hash_map = {}

        # track
        max_length = 0

        l = 0

        for r in range(len(s)):
            current_char = s[r]

            # dupe and within window
            if current_char in hash_map and hash_map[current_char] >= l:
                l = hash_map[current_char] + 1

            hash_map[current_char] = r

            curr_window_size = r - l + 1
            max_length = max(curr_window_size, max_length)

        return max_length
        
            


                



            