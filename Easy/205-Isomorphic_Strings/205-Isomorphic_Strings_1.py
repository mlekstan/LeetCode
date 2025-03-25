class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()

        for i in range(len(s)):
            if not s[i] in mapping:
                if t[i] in mapping.values():
                    return False
                else:
                    mapping[s[i]] = t[i]

            if mapping[s[i]] != t[i]:
                return False

        return True

s = "paper"
t = "title"
print(Solution().isIsomorphic(s, t))