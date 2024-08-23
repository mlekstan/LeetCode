class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        items = set()
        max = 0

        for n in range(len(s)-1, -1, -1):
            for m in range(len(s)-n):
                k = s[m:n+(m+1)]
                prev_len = 0
                for i in range(len(k)):
                    items.add(k[i])
                    if len(items) > prev_len:
                        prev_len += 1
                    else:
                        break
                
                if len(items) > max:
                    max = len(items)

                items.clear()

        return max

x = Solution().lengthOfLongestSubstring("")

print(x)