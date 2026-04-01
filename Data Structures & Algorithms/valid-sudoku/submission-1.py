class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # have to use hashsets -> distinary with each value as a set
        row_dict = {}
        col_dict = {}
        squares = {}
        # o(n)
        for i in range(len(board)):
            row_dict[i], col_dict[i] = set(), set()
        
        # o(1)
        for i in range(3):
            for j in range(3):
                squares[(i, j)] = set()
        
        # iterate thru sudoku and
        # check for dupl inside rows, cols, or squares
        # else add curr into all 3 sets
        for i in range(len(board)):
            for j in range(len(board)):
                curr = board[i][j]

                # skip if curr empty 
                if curr == ".":
                    continue

                # check for row dupl
                if curr in row_dict[i]:
                    return False
                else:
                    row_dict[i].add(curr)

                # check for col dupl
                if curr in col_dict[j]:
                    return False
                else:
                    col_dict[j].add(curr)

                # check for 3x3 dupl
                if curr in squares[(i//3, j//3)]:
                    return False
                else:
                    squares[(i//3, j//3)].add(curr)
        
        return True

                

        