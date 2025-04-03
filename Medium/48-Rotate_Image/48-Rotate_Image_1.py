from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # transpose matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            
            # reversing row
            matrix[i].reverse()


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
print(matrix)