class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}

        for i, string in enumerate (strs):
            sorted_str = "".join(sorted(string))

            if sorted_str in strs_dict:
                strs_dict[sorted_str].append(string)
            else:
                strs_dict[sorted_str] = []
                strs_dict[sorted_str].append(string)
            
        return list(strs_dict.values())



