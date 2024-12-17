# Levenshtein distance algorithm implementation - recursion

class Solution(object):

    def levenshtein(self, word1, word2, n, m):
        if min(n,m) == 0:
            return max(n,m)
        else: 
            one_or_zero = 1 if word1[n-1] != word2[m-1] else 0
            
            lev = min(
                    self.levenshtein(word1, word2, n-1, m) + 1,
                    self.levenshtein(word1, word2, n, m-1) + 1,
                    self.levenshtein(word1, word2, n-1, m-1) + one_or_zero
                )

            return lev
        

    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        
        return self.levenshtein(word1, word2, len1, len2)
    

word1 = "dinitropx"
word2 = "acetylzsdq"

print(f"Min number of operations to change {word2} into {word1}:", Solution().minDistance(word1, word2))
    