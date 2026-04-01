class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        res = []

        while l < r:
            add = numbers[l] + numbers[r]

            if add > target:
                r -= 1
            if add < target:
                l += 1
            if add == target:
                res.append(l+1)
                res.append(r+1)
                return res
        