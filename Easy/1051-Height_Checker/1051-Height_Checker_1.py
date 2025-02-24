#bubble sort

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def bubble_sort(heights):
            for i in range(len(heights)-1):
                for j in range(len(heights)-i-1):
                    if heights[j+1] < heights[j]:
                        heights[j], heights[j+1] = heights[j+1], heights[j]

            return heights
    

        reference = bubble_sort(heights[:])

        diff_count = 0
        for i in range(len(heights)):
            if heights[i] != reference[i]:
                diff_count += 1

        return diff_count
    
heights = [1,1,4,2,1,3]
print(Solution().heightChecker(heights))