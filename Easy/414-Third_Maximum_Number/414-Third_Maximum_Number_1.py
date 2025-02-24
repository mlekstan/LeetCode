from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        def maximum(nums, border):
            max_num = float('-inf')
            for num in nums:
                if num >= border:
                    continue
                elif num > max_num:
                    max_num = num
            return max_num

        
        max_num = float('inf')
        max_all = 0
        for i in range(8):
            max_num = maximum(nums, max_num)
            max_all = max_num if i == 0 else max_all


        return max_all if max_num == float('-inf') else max_num
        
    
nums = [1,1,2,5,6,2,4,7,3]
print(Solution().thirdMax(nums))