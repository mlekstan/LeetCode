from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = nums[0]

        j = 1
        for i in range(len(nums)):
            if nums[i] != val:
                val = nums[i]
                nums[j] = val
                j += 1
        
        return j


nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution().removeDuplicates(nums))
print(nums)