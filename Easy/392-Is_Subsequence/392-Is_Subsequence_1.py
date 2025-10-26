class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        len_s = len(s)
        len_t = len(t)

        if s == t:
            return True

        for i in range(len_t):
            if  (len_s > 0) and (t[i] == s[j]):
                j += 1
            
            if j == len_s:
                return True

        return False

s = "abc"
t = "ahbgdc" 
print(Solution().isSubsequence(s, t))