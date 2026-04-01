class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use dictionary of anagrams
        # e.g., {act: [act, cat, tca], stop: [pots, tops, stop]}
        dic = {}
        for string in strs:
            sortedListString = sorted(string)
            sortedString = ''
            for letter in sortedListString:
                sortedString += letter
            
            # add sortedString as the key into the dict, 
            # empty list as value
            if sortedString in dic:
                dic[sortedString].append(string)
            else:
                dic[sortedString] = []
                dic[sortedString].append(string)
            
        
        # now dic = {act: [act, cat, tca], stop: [pots, tops, stop]}
        # we want to extract out the values
        result = list(dic.values())
        return result
