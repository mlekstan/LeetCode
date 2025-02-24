# recursion :)
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[1:len(arr)]
        
        if len(arr) == 0:
            return [-1]
        
        new_arr = self.replaceElements(arr)
        max = arr[0]
        for i in arr:
            max = i if i > max else max
        return [max] + new_arr
        
    
arr = [17,18,5,4,6,1]
print(Solution().replaceElements(arr))