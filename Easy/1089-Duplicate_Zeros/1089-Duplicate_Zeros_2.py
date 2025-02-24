from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        length = len(arr)
        done = False
        for i in range(0, length):
            if done == True:
                done = False
                continue
            
            if arr[i] == 0:
                for j in range(length-1, i, -1):
                    arr[j] = arr[j-1]
            
                done = True
       

arr = [1,0,2,3,0,4,5,0]
Solution().duplicateZeros(arr)

print(arr)