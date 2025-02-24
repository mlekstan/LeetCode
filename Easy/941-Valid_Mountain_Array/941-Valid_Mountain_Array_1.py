from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        is_in = False
        
        if len(arr) < 3:
            return False

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if is_in == True:
                    return False
                if i < len(arr)-1:
                    continue
                else:
                    return False
            elif arr[i] < arr[i-1]:
                if i > 1:
                    is_in = True
                    continue
                else:
                    return False
            else:
                return False

        return True
    

arr = [3,5,5]
print(Solution().validMountainArray(arr))