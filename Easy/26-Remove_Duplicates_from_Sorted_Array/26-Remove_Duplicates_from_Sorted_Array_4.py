# LeetCode accepted recursion

from typing import List

class Solution:
    def aux_fun(self, n, nums):
        if n < 2:
            i = 1
            return i 

        else:
            i = self.aux_fun(n-1, nums)
            if nums[n-2] == nums[n-1]:
                return i
            else:
                nums[i] = nums[n-1]
                i += 1
                return i
    
    
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = self.aux_fun(n, nums)
        
        return i
        
        
nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution().removeDuplicates(nums))
print(nums)