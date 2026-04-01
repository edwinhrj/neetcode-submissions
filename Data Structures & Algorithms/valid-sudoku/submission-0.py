class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use set inside dictionary for fast lookup of duplicates
        rows = {}
        cols = {}
        squares = {}
        for i in range(len(board[0])):
            rows[i] = set()
            cols[i] = set()
        for r in range(3):
            for c in range(3):
                squares[(r, c)] = set()
        # check for duplicates for each indiv elem
        # inside rows, cols, or squares, else
        # add elem into all 3 dict(sets)
        for r in range(len(board[0])):
            for c in range(len(board[0])):
                elem = board[r][c]
                if elem == ".":
                    continue
                if elem in rows[r] or elem in cols[c] or elem in squares[(r//3, c//3)]:
                    return False
                else:
                    rows[r].add(elem)
                    cols[c].add(elem)
                    squares[(r//3, c//3)].add(elem)
        return True

                    