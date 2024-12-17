# Levenshtein distance algorithm implementation - iteration, O(n*m)

class Solution(object):
    
    def levenshtein(self, word1, word2, n, m):
        row1 = [i for i in range(m+1)]
        row2 = [0] * (m+1)

        for i in range(1, n+1):    
            for j in range(m+1):
                if j == 0:
                    row2[j] = i
                else:
                    one_or_zero = 1 if word2[j-1] != word1[i-1] else 0
                    
                    row2[j] = min(
                                row1[j] + 1,
                                row2[j-1] + 1,
                                row1[j-1] + one_or_zero
                            )
            row1 = row2.copy()

        return row1[m]
        

    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        
        return self.levenshtein(word1, word2, len1, len2)
    

word1 = "dinitropx"
word2 = "acetylzsdq"

print(f"Min number of operations to change {word2} into {word1}:", Solution().minDistance(word1, word2))