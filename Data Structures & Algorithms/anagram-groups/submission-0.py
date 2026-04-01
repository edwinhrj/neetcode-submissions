class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            sortedString = ''.join(sorted(string)) # creates ['a', 't', 'e']
            if sortedString in res:
                res[sortedString].append(string)
            else:
                res[sortedString] = []
                res[sortedString].append(string)
        return list(res.values())

        