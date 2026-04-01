class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotate means last element becomes first 
        # 3,4,5,6,1,2
        # 4,5,6,7
        # 4,5,0,1,2,3
        # 5,6,0,1,2,3,4
        # 7,8,0,1,2,3,4,5,6
        # m, check if m > r -> 
        # if m > r, means curr portion of array is rotated, -> l = m + 1 to find smaller portion of array
        # if m < r, means curr portion of array is not rotated -> return left most elem
        # if m = r, means 2,3,4,5,6,1 we check all alr and end at 1 -> return m

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            # if partial array is rotated, m > r which is not normal in bs
            if nums[m] > nums[r]:
                l = m + 1
            # if partial array is not rotated, cuz in sorted array, m is < r
            elif nums[m] < nums[r]:
                # shift r to m
                r = m
            # when m = r -> means check thru all, and left the right most
            else:
                return nums[m]

