class Solution:

    def encode(self, strs: List[str]) -> str:
        e_string = ''   # empty string 
        for s in strs:
            e_string += str(len(s)) + '#' + s   # delimiter
        return e_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []   # empty list
        i = 0               # index counter
        while i < len(s):   # loop through entire string
            j = i           # assign j for another counter
            while s[j] != '#':  # while not pound sign, count length of the string 
                j+=1            # for gettign number
            length = int(s[i:j])    # get the length for the string 
            i = j + 1   # start of the string word
            j = i + length  # end of the string
            decoded_list.append(s[i:j])
            i = j

        return decoded_list


        