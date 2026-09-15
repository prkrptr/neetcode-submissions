class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sublists = defaultdict(list)

        for string in strs:
            key = str(sorted(string))
            sublists[key].append(string)

        return list(sublists.values())