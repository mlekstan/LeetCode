from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_str = min(strs, key=len)
        
        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:  
                    return min_str[:i]
        
        return min_str
    
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))