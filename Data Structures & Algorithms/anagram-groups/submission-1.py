class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dictionary of lists
        res = {}

        for string in strs:
            sortedString = ''.join(sorted(string))
            # returns ['a', 't', 'e']
            if sortedString not in res:
                res[sortedString] = []
                res[sortedString].append(string)
            else:
                res[sortedString].append(string)
        
        # now res will be a dict of lists of anagrams
        # i.e., {['a', 'c', 't']: ['act', 'cat'], ...}

        return list(res.values())

