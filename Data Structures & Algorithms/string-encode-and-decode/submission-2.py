class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # account for if length is double digit
            length = int(s[i:j])
            indiv_string = s[j + 1 : j + 1 + length]
            res.append(indiv_string)
            # jump i to start of next number
            i = j + 1 + length
        return res
