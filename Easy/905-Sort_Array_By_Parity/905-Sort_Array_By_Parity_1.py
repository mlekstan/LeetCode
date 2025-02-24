from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_ptr = -1
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                if odd_ptr == -1:
                    odd_ptr = i
            
            else:
                odd_ptr = i if odd_ptr == -1 else odd_ptr
                
                nums[odd_ptr], nums[i] = nums[i], nums[odd_ptr]
                odd_ptr += 1

        return nums


nums = [3,1,2,4]
print(Solution().sortArrayByParity(nums))
