from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        customers_wealth = []
        for customer_id in range(len(accounts)):
            customers_wealth.append(sum(accounts[customer_id]))
        
        max_wealth = customers_wealth[0]
        for i in range(1, len(customers_wealth)):
            if max_wealth < customers_wealth[i]:
                max_wealth = customers_wealth[i]
        
        return max_wealth
    

accounts = [[2,8,7],[7,1,3],[1,9,5]]

print(Solution().maximumWealth(accounts))