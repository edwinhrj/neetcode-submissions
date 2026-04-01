class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # add s1 into dict
        check_s1 = {}
        check_s2 = {}
        for char in s1:
            if char not in check_s1:
                check_s1[char] = 1
            else:
                check_s1[char] += 1
        
        # add first len(s1) - 1 char from s2 into dict
        for i in range(len(s1) - 1):
            if s2[i] not in check_s2:
                check_s2[s2[i]] = 1
            else:
                check_s2[s2[i]] += 1

        # fixed sized sliding window
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            # add r to dict
            if s2[r] not in check_s2:
                check_s2[s2[r]] = 1
            else:
                check_s2[s2[r]] += 1

            # check if substring same as s1
            if check_s1 != check_s2:
                check_s2[s2[l]] -= 1

                # decrement already, need to remove the key if
                # its 0 (to match the s1 dict)
                if check_s2[s2[l]] == 0:
                    check_s2.pop(s2[l])
                l += 1
            else:
                return True
        return False


        