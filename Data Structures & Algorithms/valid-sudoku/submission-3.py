class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row_d = defaultdict(set)
        col_d = defaultdict(set)
        x3_d = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_d[i]:
                    return False
                row_d[i].add(board[i][j])
                if board[i][j] in col_d[j]:
                    return False
                col_d[j].add(board[i][j])
                if board[i][j] in x3_d[(i//3, j//3)]:
                    return False
                x3_d[(i//3, j//3)].add(board[i][j])
        return True

                

        