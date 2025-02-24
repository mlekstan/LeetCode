#counting sort

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def counting_sort(heights):
            count_dict = {}
            for num in heights:
                count_dict[num] = count_dict.get(num, 0) + 1

            max_num = heights[0]
            min_num = heights[0]
            
            for num in heights:
                if num > max_num:
                    max_num = num
                if num < min_num:
                    min_num = num

            j = 0
            for i in range(min_num, max_num+1):
                if i in count_dict:
                    for j in range(j, j + count_dict[i]):
                        heights[j] = i
                    j += 1

        reference = heights[:]
        counting_sort(reference)
        
        diff_count = 0
        for i in range(len(heights)):
            if heights[i] != reference[i]:
                diff_count += 1
        
        return diff_count

    
heights = [1,1,4,2,1,3]
print(Solution().heightChecker(heights))
