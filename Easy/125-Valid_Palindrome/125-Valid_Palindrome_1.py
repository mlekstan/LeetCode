class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_chars = { "q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0" }
        s_len = len(s)
        i = 0
        j = len(s) - 1
        n = 0
    
        while n < s_len :
            left = s[i].lower()
            right = s[j].lower()
            if (left in alpha_chars) and (right in alpha_chars):
                if left == right:
                    i += 1; j -= 1; n += 2
                    continue
                else:
                    return False
            
            if left not in alpha_chars:
                i += 1; n += 1
            
            if right not in alpha_chars:
                j -= 1; n += 1

        return True
    
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))