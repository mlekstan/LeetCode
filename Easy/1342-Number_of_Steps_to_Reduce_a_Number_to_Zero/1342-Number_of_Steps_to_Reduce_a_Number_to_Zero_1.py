# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num > 0:
            if num % 2 == 0:
                num *= 0.5
            else:
                num -= 1
            
            i += 1

        return i

print(Solution().numberOfSteps(14))