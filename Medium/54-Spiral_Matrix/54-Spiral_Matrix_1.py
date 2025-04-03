from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        def spiral(first_row_idx, last_row_idx, first_col_idx, last_col_idx):
            if first_row_idx > last_row_idx or first_col_idx > last_col_idx:
                return
            
            # First row (left to right)
            first_row = [matrix[first_row_idx][i] for i in range(first_col_idx, last_col_idx + 1)]
            
            # Last column (top to bottom)
            last_col = [matrix[i][last_col_idx] for i in range(first_row_idx + 1, last_row_idx)]
            
            # Last row (right to left) - only if there's more than one row
            last_row = [matrix[last_row_idx][i] for i in range(first_col_idx, last_col_idx + 1)][::-1] if first_row_idx < last_row_idx else []
            
            # First column (bottom to top) - only if there's more than one column
            first_col = [matrix[i][first_col_idx] for i in range(first_row_idx + 1, last_row_idx)][::-1] if first_col_idx < last_col_idx else []
            
            
            result.extend(first_row)
            result.extend(last_col)
            result.extend(last_row)
            result.extend(first_col)
            
            
            spiral(first_row_idx + 1, last_row_idx - 1, first_col_idx + 1, last_col_idx - 1)
        
        spiral(0, len(matrix) - 1, 0, len(matrix[0]) - 1)
        return result
    

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))