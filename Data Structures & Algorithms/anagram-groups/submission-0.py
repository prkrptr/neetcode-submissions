class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arr = {}    # initialize empty  key : index value
        for word in strs:
            sorted_string = ''.join(sorted(word))

            if sorted_string not in arr:
                arr[sorted_string] = []  # put an empty list

            arr[sorted_string].append(word)

        return list(arr.values())
            

            

