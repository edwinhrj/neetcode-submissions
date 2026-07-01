class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search, since array is broken into 2 independently 
        # sorted arrays, m will always land within either of the 2 sorted sub arrays

        # if m in left sorted array, do the logic, 
        # if m in right sorted array, do the logic

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # if m in left sorted array
            if nums[l] <= nums[m]:
                if target > nums[m]:
                    # search right of m
                    l = m + 1
                else:
                    # check if target smaller than l, 
                    if target < nums[l]:
                        # search right
                        l = m + 1
                    else:
                        # search left
                        r = m - 1
            
            # if m in right sorted array
            if nums[m] <= nums[r]:
                if target > nums[m]:
                    if target <= nums[r]:
                        # search right array
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1
        return -1
