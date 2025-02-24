from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ptr = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if ptr == -1:
                    ptr = i
            elif ptr == -1:
                continue
            else:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr += 1
            
            
                
nums = [2,0,1,0,5,7]
Solution().moveZeroes(nums)
print(nums)