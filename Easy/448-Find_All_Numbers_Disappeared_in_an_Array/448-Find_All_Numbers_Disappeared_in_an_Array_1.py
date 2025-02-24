from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        diff = []
        for i in range(1, len(nums)+1):
            if i not in nums_set:
                diff.append(i)

        return diff
        

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))