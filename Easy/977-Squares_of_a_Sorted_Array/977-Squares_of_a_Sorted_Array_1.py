# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        i = 0
        j = len(nums)-1
        loop_count = 0
        
        while i < j:
            if abs(nums[i]) > abs(nums[j]):
                arr[-1 - loop_count] = nums[i]**2
                i += 1
            else:
                arr[-1 - loop_count] = nums[j]**2
                j -= 1
            
            loop_count += 1

        arr[0] = nums[i]**2

        return arr
    

nums = [-7,-3,2,3,11]
print(Solution().sortedSquares(nums))
