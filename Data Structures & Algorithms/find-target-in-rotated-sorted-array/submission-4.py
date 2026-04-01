class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search
        # 3,4,5,6,1,2
        # 3,4,5,6,1,2
        # 6,7,0,1,2,3,4,5
        # 1,2,3,4,5,6,7
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                # have to find portion that is less than m
                if target >= nums[l]:
                    r = m - 1
                # check if target < l, depends where the pivot is
                else:
                    # left side is normally sorted, means target is not herer
                    # can go right
                    if nums[l] <= nums[m]:
                        l = m + 1
                    else:
                    # if left side has the pivot, the small numbers are here
                        r = m - 1
            elif target > nums[m]:
                # have to find portion that is nmore than m
                # check if target < nums[r], means its within
                # the portion at right
                if target <= nums[r]:
                    l = m + 1
                # if target is larger than m and larger than r
                else:
                    # have to check where the pivot is still
                    if nums[m] <= nums[l]:
                        # means right is sorted normally
                        # check left portion
                        r = m - 1
                    else:
                        # means right has the pivot
                        # check right
                        l = m + 1
            else:
                return m
        return -1