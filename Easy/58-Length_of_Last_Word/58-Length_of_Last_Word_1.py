class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and length > 0:
                break
            elif s[i] == " ":
                continue
            else:
                length += 1
        return length

s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))