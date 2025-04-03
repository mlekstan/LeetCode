from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = matrix.pop(0)
        if not matrix:
            return result

        rotated_matrix = list(map(list, zip(*matrix)))
        rotated_matrix = rotated_matrix[::-1]

        return result + self.spiralOrder(rotated_matrix)
    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))