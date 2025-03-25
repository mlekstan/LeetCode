from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        n = len(nums)

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > (n // 2):
                return num
            
nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))