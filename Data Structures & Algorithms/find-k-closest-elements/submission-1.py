# Shrinking Window / Two-Pointer Approach
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        
        # Shrink the window one element at a time until only k remain
        while right - left >= k:
            if x - arr[left] > arr[right] - x:
                left += 1  # Left element is further, discard it
            else:
                right -= 1 # Right element is further (or equal), discard it
                
        return arr[left:right + 1]