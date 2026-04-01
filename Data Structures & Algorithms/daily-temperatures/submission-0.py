class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        # brute force
        res = []
        for l in range(len(t)):
            for r in range(l + 1, len(t)):
                if t[r] > t[l]:
                    res.append(r - l)
                    break
            # if larger number has not been found
            if len(res) < l + 1:
                res.append(0)
        return res
            
        

                
                
