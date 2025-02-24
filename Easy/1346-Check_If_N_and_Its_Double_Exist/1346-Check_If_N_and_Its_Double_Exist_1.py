from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if i == j:
                    continue

                if arr[i] == 2*arr[j]:
                    return True
                
        return False

arr = [10,2,5,3]
print(Solution().checkIfExist(arr))