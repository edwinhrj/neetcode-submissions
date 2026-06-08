class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # iterate thru and store change
        from collections import defaultdict
        change = defaultdict(int)
        for b in bills:
            if b == 5:
                change[5] += 1
            elif b == 10:
                if change[5] >= 1:
                    change[10] += 1
                    change[5] -= 1
                else:
                    return False
            else:
                # use up 10 + 5 bill first before 5,5,5 bill
                if change[10] >= 1 and change[5] >= 1: 
                    change[20] += 1
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[20] += 1
                    change[5] -= 3
                else:
                    return False
        return True
            
                
                