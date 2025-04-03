from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_arr_valid(arr: List[str]):
            seen = set()
            for item in arr:
                if item in seen and item != ".":
                    return False
                seen.add(item)
            return True

        # check rows
        for row in board:
            if not is_arr_valid(row):
                return False
            
        # matrix transposition
        t_board = []
        for i in range(len(board[0])):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            t_board.append(col)

        # check columns
        for row in t_board:
            if not is_arr_valid(row):
                return False
        
        for m in range(0, 9, 3):
            for k in range(0, 9, 3):
                box_arr = []
                for i in range(3):
                    row = board[i+m]
                    for j in range(3):
                        box_arr.append(row[j+k])
                if not is_arr_valid(box_arr):
                    return False
                
        return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))
            

                       