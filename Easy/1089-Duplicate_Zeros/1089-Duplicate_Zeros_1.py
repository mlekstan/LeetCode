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
                mem = None
                for j in range(i+1, length):
                    if j == i+1:
                        mem = arr[j]
                        arr[j] = arr[j-1]
                    else:
                        temp = arr[j]
                        arr[j] = mem
                        mem = temp

                done = True
            

arr = [1,0,2,3,0,4,5,0]
Solution().duplicateZeros(arr)

print(arr)