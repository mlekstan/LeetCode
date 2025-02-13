# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        letters = {}
        
        for char in magazine:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        for char in ransomNote:
            if char in letters:
                letters[char] -= 1
            else:
                return False
                
            if letters[char] < 0:
                return False
            
        return True


ransomNote = "a"
magazine = "b"

print(Solution().canConstruct(ransomNote, magazine))