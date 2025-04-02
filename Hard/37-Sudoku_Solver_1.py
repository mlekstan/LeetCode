from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        height = len(board)
        width = len(board[0])

        def is_good(row_ptr, col_ptr, digit):
            # check row
            for i in range(width):
                if i != col_ptr and board[row_ptr][i] == digit:
                    return False
                
            # check column
            for i in range(height):
                if i != row_ptr and board[i][col_ptr] == digit:
                    return False
                
            # check 3x3 box
            start_row_ptr = row_ptr//3 * 3
            start_col_ptr = col_ptr//3 * 3

            for i in range(start_row_ptr, start_row_ptr+3):
                for j in range(start_col_ptr, start_col_ptr+3):
                    if i != row_ptr and j != col_ptr and board[i][j] == digit:
                        return False
                    
            return True


        def fill_in(row_ptr, col_ptr):    
            if row_ptr == height:
                return True
            
            next_row_ptr = row_ptr + 1 if col_ptr == width-1 else row_ptr
            next_col_ptr = 0 if col_ptr == width-1 else col_ptr+1

            if board[row_ptr][col_ptr] == ".":
                for digit in range(1, 10):
                    if is_good(row_ptr, col_ptr, str(digit)):
                        
                        board[row_ptr][col_ptr] = str(digit)
                        
                        if fill_in(next_row_ptr, next_col_ptr):
                            return True
                        board[row_ptr][col_ptr] = "."
                return False
            else:
                return fill_in(next_row_ptr, next_col_ptr)
                    
        fill_in(0,0)


board = [[".",".",".",".",".",".",".",".","."],
         [".","9",".",".","1",".",".","3","."],
         [".",".","6",".","2",".","7",".","."],
         [".",".",".","3",".","4",".",".","."],
         ["2","1",".",".",".",".",".","9","8"],
         [".",".",".",".",".",".",".",".","."],
         [".",".","2","5",".","6","4",".","."],
         [".","8",".",".",".",".",".","1","."],
         [".",".",".",".",".",".",".",".","."]]

Solution().solveSudoku(board)
for row in board:
    print(row)




