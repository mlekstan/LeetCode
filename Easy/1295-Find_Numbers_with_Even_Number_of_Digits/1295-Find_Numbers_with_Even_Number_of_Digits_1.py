# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            digits_count = 0
            while num >= 1:
                num *= 0.1
                digits_count += 1
            
            if digits_count % 2 == 0:
                even_count += 1
                
        return even_count
    

nums = [12,345,2,6,7896]
print(Solution().findNumbers(nums))