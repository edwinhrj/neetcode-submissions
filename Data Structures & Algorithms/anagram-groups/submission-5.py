class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # just use 1 dictionary
        # sorted(string) is immutable and can be key to dict
        # iterate thru strs and store s in sublist in dict, 
        # using sorted(string) as key
        # list(dict.values())

        d = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in d:
                d[key] = []
                d[key].append(s)
            else:
                d[key].append(s)
        
        return list(d.values())