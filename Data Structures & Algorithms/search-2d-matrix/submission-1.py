class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search each row,
        # if targer larger than end of curr row, 
        # move on to the next row and binary search again

        i = 0
        while i < len(matrix):
            # if target is larger than the 
            # last element of the curr row, 
            # skip to next row
            if target > matrix[i][-1]:
                i += 1
                continue
            
            l, r = 0, len(matrix[i]) - 1
            while l <= r:
                m = (r + l) // 2
                if target < matrix[i][m]:
                    r = m - 1
                elif target == matrix[i][m]:
                    return True    
                else:
                    l = m + 1
            # if target has passed thru all 
            # checks in curr row and still 
            # not found/not moved on to next row
            return False
        return False
            
