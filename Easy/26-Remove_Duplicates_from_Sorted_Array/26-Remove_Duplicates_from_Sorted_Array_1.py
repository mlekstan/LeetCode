from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        val = nums[0]
        while i < len(nums):
            if nums[i] == val :
                i += 1
            else:
                nums[j] = val
                j += 1
                val = nums[i]
        
        nums[j] = val

        return j + 1


nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution().removeDuplicates(nums))
print(nums)