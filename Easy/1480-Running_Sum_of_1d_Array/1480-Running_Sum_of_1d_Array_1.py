from typing import List

class Solution:
    def runningSum(self, n, nums: List[int]) -> List[int]:
        
        if n < 2:
            return nums[n-1] 

        nums[n-1] = self.runningSum(n-1, nums) + nums[n-1]
        
        return nums[n-1]

nums = [3,1,2,10,1]
n = len(nums)

Solution().runningSum(n, nums)

print(nums)
