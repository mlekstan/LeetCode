class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx_list = []
        first_occurance = 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                idx_list.append(i)
        
        for start_idx in idx_list:
            for i in range(len(needle)):
                first_occurance = start_idx
                if not (start_idx + i < len(haystack) and haystack[start_idx+i] == needle[i]):
                    break
                
                if i == len(needle) - 1:
                    return first_occurance 
        return -1
    
haystack = "mississippi"
needle = "issip"

print(Solution().strStr(haystack, needle))