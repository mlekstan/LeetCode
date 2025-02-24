from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero_count = 0
        for i in arr:
            if i == 0:
                zero_count += 1
        
        for i in range(0, len(arr)):
            if 2*arr[i] in arr:
                if arr[i] == 0 and zero_count == 1:
                    continue
                else:
                    return True
        return False
            

arr = [10,2,5,3]
print(Solution().checkIfExist(arr))