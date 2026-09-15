class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num_set = set()
        l =0
        longest_length = 0
        for r in range(len(s)):
            while s[r] in num_set:
                num_set.remove(s[l])
                l+=1
            
            num_set.add(s[r])
            longest_length = max(longest_length, r - l + 1)

        return longest_length