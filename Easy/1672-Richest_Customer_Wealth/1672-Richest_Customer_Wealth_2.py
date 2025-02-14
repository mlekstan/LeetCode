# Only recursion :-)

from typing import List

class Solution:
    def sum(self, list: List[int]) -> int:
        if len(list) < 2:
            return list[0]
        
        sum = self.sum(list[:-1]) + list[-1]
        
        return sum
    
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if len(accounts) < 2:
            return self.sum(accounts[0])

        max = self.maximumWealth(accounts[:-1])
        sum = self.sum(accounts[-1])
        
        if max < sum:
            max = sum    
        
        return max
    

accounts = [[2,8,7],[7,1,3],[1,9,5]]

print(Solution().maximumWealth(accounts))