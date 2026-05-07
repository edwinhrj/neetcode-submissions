class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        
        # Binary search for the left bound of our size-k window
        while left < right:
            mid = (left + right) // 2
            
            # Compare distance of the start of the window vs the element just past the window
            if x - arr[mid] > arr[mid + k] - x:
                # The right side is closer or equally close, so the window must start further right
                left = mid + 1
            else:
                # The left side is closer, so the window can't start further right than mid
                right = mid
                
        return arr[left:left + k]