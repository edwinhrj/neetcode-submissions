from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if target < nums[m]:
                # If target is between l and m, it's definitely on the left
                if target >= nums[l]:
                    r = m - 1
                # If target < nums[l], it depends on where the pivot is
                else:
                    # If left half is normally sorted, target is too small to be here -> go right
                    if nums[l] <= nums[m]:
                        l = m + 1
                    # If left half has the pivot, the small numbers are actually here -> go left
                    else:
                        r = m - 1
                        
            elif target > nums[m]:
                # If target is between m and r, it's definitely on the right
                if target <= nums[r]:
                    l = m + 1
                # If target > nums[r], it depends on where the pivot is
                else:
                    # If right half is normally sorted, target is too big to be here -> go left
                    if nums[m] <= nums[r]:
                        r = m - 1
                    # If right half has the pivot, the big numbers are actually here -> go right
                    else:
                        l = m + 1
                        
            else:
                return m
                
        return -1