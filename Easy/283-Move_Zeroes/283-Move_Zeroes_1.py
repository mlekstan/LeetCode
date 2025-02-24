from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_pointer = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
                zero_pointer += 1 
            
            
                
nums = [2,0,1,0,5,7]
Solution().moveZeroes(nums)
print(nums)