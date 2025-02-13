# https://leetcode.com/problems/max-consecutive-ones/description/

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = count if count > max_count else max_count
            else:
                count = 0
        
        return max_count
    

nums = [1,0,1,1,0,1]
print(Solution().findMaxConsecutiveOnes(nums))