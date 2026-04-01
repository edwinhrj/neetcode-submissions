class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        unique = set(nums)
        max_len = 0
        # 2, 20, 4, 10, 3, 5
        for num in unique:
            # means num is start of sequence
            if num - 1 not in unique:
                curr_len = 1
                while num + 1 in unique:
                    curr_len += 1
                    num += 1
                max_len = max(max_len, curr_len)
        return max_len




