# LeetCode not accepted recursion but solution is good, 
# solution: 26-Remove_Duplicates_from_Sorted_Array_4.py
# allows to overcome obstacles created by LeetCode

from typing import List

class Solution:
    def removeDuplicates(self, n, nums: List[int]) -> int:
        if n < 2:
            i = 1
            return i 

        else:
            i = self.removeDuplicates(n-1, nums)
            if nums[n-2] == nums[n-1]:
                return i
            else:
                nums[i] = nums[n-1]
                i += 1
                return i
            

nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution().removeDuplicates(len(nums), nums))
print(nums)