
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        total = 0
        
        for i in range(len(word)):
            seen_vowels = set()
            cons_count = 0
            j = i
            while j < len(word):
                if word[j] in vowels:
                    seen_vowels.add(word[j])
                else:
                    cons_count += 1

                j += 1

                if cons_count == k and seen_vowels == vowels:
                    total += 1
                elif cons_count > k:
                    break

        return total
    
word = "iqeaouqi"
print(Solution().countOfSubstrings(word, 2))