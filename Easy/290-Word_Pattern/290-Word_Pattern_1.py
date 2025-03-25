class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split()
        if len(pattern) != len(s_arr):
            return False

        mapping = dict()
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != s_arr[i]:
                    return False
            else:
                if s_arr[i] in mapping.values():
                    return False
                else:
                    mapping[pattern[i]] = s_arr[i]

        return True