class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        s1_counts, s2_counts = [0] * 26, [0] * 26

        # add in the counts of the s1 word in BOTH
        # s1 and s
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        # check if initial first n1 letters are anagrams of eo
        if s1_counts == s2_counts:
            return True

        # fixed size sliding window
        for r in range(n1, n2):
            # add char to substring_count
            index = ord(s2[r]) - ord('a')
            s2_counts[ord(s2[r]) - ord('a')] += 1
            # remove left most to keep window size fixed
            s2_counts[ord(s2[r - n1]) - ord('a')] -= 1
            if s1_counts == s2_counts:
                return True 
        
        return False
