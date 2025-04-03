
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        total = 0
        vowels_count = {}
        left = 0
        right = 0
        cons_count = 0
        next_cons = [0] * len(word)
        next_cons_idx = len(word)

        for i in range(len(word)-1, -1, -1):
            next_cons[i] = next_cons_idx
            if word[i] not in vowels:
                next_cons_idx = i

        while right < len(word):
            if word[right] not in vowels:
                cons_count += 1
            else:
                vowels_count[word[right]] = vowels_count.get(word[right], 0) + 1

            while (cons_count > k):
                if word[left] not in vowels:
                    cons_count -= 1
                else:
                    vowels_count[word[left]] -= 1
                    if vowels_count[word[left]] == 0:
                        del vowels_count[word[left]]
                left += 1

            while (left < len(word) and len(vowels) == len(vowels_count) and cons_count == k):
                total += next_cons[right] - right
                if word[left] not in vowels:
                    cons_count -= 1
                else:
                    vowels_count[word[left]] -= 1
                    if vowels_count[word[left]] == 0:
                        del vowels_count[word[left]]
                left += 1

            right += 1
    
        return total

    
word = "iqeaouqi" 
print(Solution().countOfSubstrings(word, 2))