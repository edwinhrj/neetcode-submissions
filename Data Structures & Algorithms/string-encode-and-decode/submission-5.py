class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while s:
            count = ''
            for i in range(len(s)):
                if s[i] != '#':
                    count += s[i]
                else:
                    count = int(count)
                    start = i + 1
                    break
            string = s[start:count + start]
            res.append(string)
            s = s[start+count:]
        return res
            



