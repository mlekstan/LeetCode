# Full solution but it has not to look like that - there is no need to care about last numbers in final array (numbers which are deleted).
# In this soulution all numbers that should be deleted are gathered on the end of the array. Solution bases on the partition() function
# that is part of quicksort algorithm.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        size = len(nums)
        
        if size == 0:
            return 0
        
        num_del = 0
        i = 0
        j = size - 1

        while True:
            while nums[i] != val:
                i += 1
                if i >= size:
                    break
            
            while nums[j] == val:
                num_del += 1
                j -= 1
                if j < 0:
                    break

            if i < j:
                nums[i] = nums[j]
                nums[j] = val
                num_del += 1

                i += 1
                j -= 1
            else:
                return size - num_del
            

nums = [0,1,2,2,3,0,4,2]

print(Solution().removeElement(nums, 2))
print(nums)