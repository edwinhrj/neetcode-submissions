class Solution:

    # ['hello', 'world'] -> '05#hello05#world'
    def encode(self, strs: List[str]) -> str:
        res = ''
        delimiter = '#'
        for word in strs:
            res += str(len(word)) + delimiter + word
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        delimiter = '#'
        # shift and change based on the length 
        # to get o(n) complexity instead of using full iteration
        i = 0
        # while pointer is within the length of string
        while i < len(s):
            j = i
            # loop till pointer is at delimiter
            while s[j] != delimiter:
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : length + j + 1]
            res.append(word) # add word back to list
            i = j + 1 + length  # reset i to the start of next number
        return res



                
